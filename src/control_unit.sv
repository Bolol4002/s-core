module control_unit(input a, input b, output y);
   assign y = ~(a & b);
endmodule
