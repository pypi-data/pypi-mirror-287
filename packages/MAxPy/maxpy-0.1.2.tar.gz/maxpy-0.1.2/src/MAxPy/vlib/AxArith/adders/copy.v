module copyA #(
  parameter BIT_WIDTH=8,
  parameter K=5
)(

  input    [BIT_WIDTH-1:0] A,B,
  output   [BIT_WIDTH:0] OUT
);
  generate
    if (K == 0) begin
      assign OUT = A + B;
    end else begin
      assign OUT[BIT_WIDTH:K] = A[BIT_WIDTH-1:K] + B[BIT_WIDTH-1:K];
      assign OUT[K-1:0] = A[K-1:0];
    end
  endgenerate
endmodule

module copyB #(
  parameter BIT_WIDTH=8,
  parameter K=5
)(

  input    [BIT_WIDTH-1:0] A,B,
  output   [BIT_WIDTH:0] OUT
);
  generate
    if (K == 0) begin
      assign OUT = A + B;
    end else begin
      assign OUT[BIT_WIDTH:K] = A[BIT_WIDTH-1:K] + B[BIT_WIDTH-1:K];
      assign OUT[K-1:0] = B[K-1:0];
    end
  endgenerate
endmodule
