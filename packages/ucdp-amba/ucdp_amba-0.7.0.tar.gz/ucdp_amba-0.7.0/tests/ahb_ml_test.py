#
# MIT License
#
# Copyright (c) 2024 nbiotcloud
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

"""
Unified Chip Design Platform - AMBA - AHB Tests.
"""

import logging
import random

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Combine, RisingEdge

from tests.ahb_driver import AHBMasterDriver, AHBSlaveDriver, BurstType, SizeType


def _calc_wrmem(offs: int, size: SizeType, blen: int, mmask: int, wdata: list[int]) -> bytearray:
    """Calculate Reference Write Data in Bytes."""
    memimg = bytearray(blen << size)
    for widx in range(blen):
        midx = (offs + (widx << size)) & mmask
        memimg[midx : (midx + (1 << size))] = int.to_bytes(wdata[widx], 1 << size, "little")
    return memimg


def _calc_expected(offs: int, size: SizeType, blen: int, mmask: int, mem: bytearray) -> list[int]:
    """Calculate Expected Read Data."""
    xdata = []
    for widx in range(blen):
        xd = 0
        for bidx in range(1 << size):
            xd |= mem[(offs & ~mmask) + ((offs + (widx << size) + bidx) & mmask)] << (bidx << 3)
        xdata.append(xd)
    return xdata


# TODO put this is a generic tb lib
async def wait_clocks(clock, cycles):
    """Helper Function."""
    for _ in range(cycles):
        await RisingEdge(clock)


@cocotb.test()
async def ahb_ml_test(dut):
    """Main Test Loop."""
    log = logging.getLogger(__name__)
    log.setLevel(logging.INFO)

    hclk = dut.main_clk_i
    rst_an = dut.main_rst_an_i

    ext_mst = AHBMasterDriver(
        name="ext_mst",
        log_level=logging.INFO,
        clk=hclk,
        rst_an=rst_an,
        haddr=dut.ahb_mst_ext_haddr_i,
        hwrite=dut.ahb_mst_ext_hwrite_i,
        hwdata=dut.ahb_mst_ext_hwdata_i,
        htrans=dut.ahb_mst_ext_htrans_i,
        hburst=dut.ahb_mst_ext_hburst_i,
        hsize=dut.ahb_mst_ext_hsize_i,
        hprot=dut.ahb_mst_ext_hprot_i,
        hrdata=dut.ahb_mst_ext_hrdata_o,
        hready=dut.ahb_mst_ext_hready_o,
        hresp=dut.ahb_mst_ext_hresp_o,
        hsel=None,
    )

    dsp_mst = AHBMasterDriver(
        name="dsp_mst",
        log_level=logging.INFO,
        clk=hclk,
        rst_an=rst_an,
        haddr=dut.ahb_mst_dsp_haddr_i,
        hwrite=dut.ahb_mst_dsp_hwrite_i,
        hwdata=dut.ahb_mst_dsp_hwdata_i,
        htrans=dut.ahb_mst_dsp_htrans_i,
        hburst=dut.ahb_mst_dsp_hburst_i,
        hsize=dut.ahb_mst_dsp_hsize_i,
        hprot=dut.ahb_mst_dsp_hprot_i,
        hrdata=dut.ahb_mst_dsp_hrdata_o,
        hready=dut.ahb_mst_dsp_hready_o,
        hresp=dut.ahb_mst_dsp_hresp_o,
        hsel=None,
    )

    ram_slv = AHBSlaveDriver(
        name="ram_slv",
        log_level=logging.INFO,
        clk=hclk,
        rst_an=rst_an,
        hsel=dut.ahb_slv_ram_hsel_o,
        haddr=dut.ahb_slv_ram_haddr_o,
        hwrite=dut.ahb_slv_ram_hwrite_o,
        htrans=dut.ahb_slv_ram_htrans_o,
        hsize=dut.ahb_slv_ram_hsize_o,
        hburst=dut.ahb_slv_ram_hburst_o,
        hprot=dut.ahb_slv_ram_hprot_o,
        hwdata=dut.ahb_slv_ram_hwdata_o,
        hready=dut.ahb_slv_ram_hready_o,
        hreadyout=dut.ahb_slv_ram_hreadyout_i,
        hresp=dut.ahb_slv_ram_hresp_i,
        hrdata=dut.ahb_slv_ram_hrdata_i,
    )

    cocotb.start_soon(Clock(hclk, period=10).start())

    cocotb.start_soon(ram_slv.run())

    # initial reset
    rst_an.value = 0
    await wait_clocks(hclk, 10)
    rst_an.value = 1
    await wait_clocks(hclk, 10)

    await dsp_mst.write(0xF0000300, 0xBEEFBEEF)
    await wait_clocks(hclk, 5)

    ext_wr = cocotb.start_soon(ext_mst.write(0xF0000300, 0x76543210))
    dsp_wr = cocotb.start_soon(
        dsp_mst.write(0xF0000316, (0x11, 0x22, 0x33, 0x44), burst_type=BurstType.WRAP4, size=SizeType.HALFWORD)
    )
    await Combine(ext_wr, dsp_wr)
    await wait_clocks(hclk, 5)
    ram_slv.log_data()

    # ext_wr = cocotb.start_soon(ext_mst.write(0xF0000000, 0x76543210))
    # dsp_wr = cocotb.start_soon(
    #     dsp_mst.write(0xF0000016, (0x11, 0x22, 0x33, 0x44), burst_type=BurstType.WRAP4, size=SizeType.HALFWORD)
    # )
    # await Combine(ext_wr, dsp_wr)

    # await wait_clocks(hclk, 5)
    # rdata = await ext_mst.read(0xF0000000, burst_type=BurstType.INCR8, size=SizeType.BYTE)
    # print("MST EXT rdata:", [hex(data) for data in rdata])
    # await wait_clocks(hclk, 5)

    mem = bytearray(1024)
    btypes = (
        BurstType.SINGLE,
        BurstType.WRAP4,
        BurstType.INCR4,
        BurstType.WRAP8,
        BurstType.INCR8,
        BurstType.WRAP16,
        BurstType.INCR16,
    )
    sizes = (SizeType.BYTE, SizeType.HALFWORD, SizeType.WORD)
    for _ in range(20):
        btype = random.choice(btypes)
        size = random.choice(sizes)
        if btype == BurstType.SINGLE:
            blen = 1
            mmask = (1 << size) - 1
        else:
            blen = 2 << (btype >> 1)
            mmask = (4 << (((btype - 2) >> 1) + size)) - 1
        offs = random.randint(0, 511) & ~((1 << size) - 1)  # make it size aligned

        if btype in (BurstType.INCR16, BurstType.INCR8, BurstType.INCR4):
            offs &= ~mmask  # make it burst aligned
        smax = (1 << (1 << (size + 3))) - 1  # max value according to size
        if random.randint(0, 1):
            wdata = [random.randint(1, smax) for i in range(blen)]

            mem[(offs & ~mmask) : (offs & ~mmask) + (blen << size)] = _calc_wrmem(
                offs=offs, size=size, blen=blen, mmask=mmask, wdata=wdata
            )
            log.info(
                f"=MST WRITE TRANSFER= offs:{hex(offs)}; burst:{btype.name}; size:{size.name}; "
                f"wdata:{[hex(w) for w in wdata]}"
            )
            await ext_mst.write(0xF0000000 + offs, wdata, burst_type=btype, size=size)
        else:
            xdata = _calc_expected(offs=offs, size=size, blen=blen, mmask=mmask, mem=mem)
            rdata = await ext_mst.read(0xF0000000 + offs, burst_type=btype, size=size)
            if tuple(rdata) == tuple(xdata):
                log.info(
                    f"=MST READ TRANSFER= offs:{hex(offs)}; burst:{btype.name}; size:{size.name};\n"
                    f"> rdata: {[hex(w) for w in rdata]};"
                )
            else:
                log.error(
                    f"=MST READ TRANSFER MISMATCH= offs:{hex(offs)}; burst:{btype.name}; size:{size.name};\n"
                    f"> expected: {[hex(w) for w in xdata]};\n"
                    f"> got:      {[hex(w) for w in rdata]};"
                )
                raise AssertionError("Read data compare mismatch.")

        await wait_clocks(hclk, 2)

    await wait_clocks(hclk, 30)
