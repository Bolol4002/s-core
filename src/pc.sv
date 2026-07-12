module pc (
    input  logic        clk,
    input  logic        rst,
    input  logic [31:0] next_pc,
    output logic [31:0] pc_o
);

    always_ff @(posedge clk) begin
        if (rst)
            pc_o <= 32'd0;
        else
            pc_o <= next_pc;
    end

endmodule