module dmem (
    input logic clk,

    input logic mem_write,
    input logic mem_read,

    input logic [31:0] addr,
    input logic [31:0] write_data,

    output logic [31:0] read_data
);

    logic [31:0] mem [0:255];

    always_ff @(posedge clk) begin
        if (mem_write) begin
            mem[addr[9:2]] <= write_data;
        end
    end

    assign read_data = mem[addr[9:2]];

endmodule
