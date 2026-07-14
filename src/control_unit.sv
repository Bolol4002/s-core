import cpu_pkg::*;

module control_unit (
    input  logic [6:0] opcode,

    output logic reg_write,
    output logic alu_src,
    output logic mem_read,
    output logic mem_write,
    output logic mem_to_reg,
    output logic branch,
    output logic jump
);

    always_comb begin
        // Default control signals
        reg_write = 1'b0;
        alu_src   = 1'b0;
        mem_read  = 1'b0;
        mem_write = 1'b0;
        mem_to_reg = 1'b0;
        branch    = 1'b0;
        jump      = 1'b0;

        unique case (opcode)

            OPCODE_RTYPE: begin
                reg_write = 1'b1;
            end

            default: ;

        endcase
    end

endmodule