pac_base = {
    "config_name": "pac_base",

    "rtl_files": [],

    "rtl_incdirs": ["include/"],

    "rtl_dependencies": [
        "/include/common_cells/assertions.svh",
        "/include/common_cells/registers.svh",
        "/src/cf_math_pkg.sv",
        "/src/stream_mux.sv",
        "/src/stream_fork.sv",
        "/src/stream_fifo.sv",
        "/src/stream_to_mem.sv",
        "/src/mem_to_banks_detailed.sv",
        "/src/stream_join.sv",
        "/src/stream_fork_dynamic.sv",
        "/src/stream_join_dynamic.sv",
        "/src/fifo_v3.sv",
        "/src/addr_decode.sv",
        "/src/addr_decode_dync.sv",
        "/src/spill_register.sv",
        "/src/spill_register_flushable.sv",
        "/src/counter.sv",
        "/src/delta_counter.sv",
        "/src/rr_arb_tree.sv",
        "/src/stream_register.sv",
        "/src/lzc.sv",
    ],

    "tb_files": [],

    "tb_incdirs": [],

    "tb_dependencies": [], #TODO The TB is based on the old DSL library so it needs ddl as well

    "verilog_wrapper": "",

    "variants": [],

}