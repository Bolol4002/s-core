module fpga_top (
    input  logic        clk,
    input  logic        rst,
    output logic [15:0] led
);

    logic [31:0] alu_result;
    logic        zero;

    // Clock divider: ~1 Hz for visible LED blinking
    // 100 MHz / 2^26 ≈ 1.49 Hz
    logic [25:0] counter;
    logic        slow_clk;

    always_ff @(posedge clk or posedge rst) begin
        if (rst)
            counter <= 26'd0;
        else
            counter <= counter + 26'd1;
    end

    assign slow_clk = counter[25];

    // CPU instance
    cpu u_cpu (
        .clk(slow_clk),
        .rst(rst),
        .alu_result(alu_result),
        .zero(zero)
    );

    // Drive LEDs with lower 16 bits of ALU result
    assign led = alu_result[15:0];

endmodule
