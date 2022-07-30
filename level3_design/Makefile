# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/Traffic_Light_controller.v              # provide your design path

TOPLEVEL := Traffic_Light_controller   # design file
MODULE   := test_traffic_light    # test file

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
