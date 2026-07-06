module regfile (

    input  logic        clk,
    input  logic        we,

    input  logic [4:0]  rs1_addr,
    input  logic [4:0]  rs2_addr,

    input  logic [4:0]  rd_addr,
    input  logic [31:0] rd_data,

    output logic [31:0] rs1_data,
    output logic [31:0] rs2_data

);
   logic [31:0] mem [31:0];
   always_ff @(posedge clk) begin
      if (we && rd_addr!=0)
        mem[rd_addr]<=rd_data;
   end

   always_comb begin
      rs1_data = (rs1_addr==5'd0)?32'd0:mem[rs1_addr];
      rs2_data = (rs2_addr==5'd0)?32'd0:mem[rs2_addr];
   end
endmodule // regfile
