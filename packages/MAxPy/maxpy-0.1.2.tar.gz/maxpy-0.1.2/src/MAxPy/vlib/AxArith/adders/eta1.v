module eta1 #(
  parameter BIT_WIDTH=8,
  parameter K=5
)(
  input    [BIT_WIDTH-1:0] A,B,
  output   [BIT_WIDTH:0] OUT
);


  genvar i;
  generate
    if (K == 0) begin
      assign OUT = A + B;
    end
    else begin
      wire [K-1:0] P, G, SET_CMD;
      assign OUT[BIT_WIDTH:K] = A[BIT_WIDTH-1:K] + B[BIT_WIDTH-1:K];

      for (i = 0; i < K; i = i + 1)begin
        assign G[i] = A[i] & B[i];
        assign P[i] = A[i] ^ B[i];
      end

      assign SET_CMD[K-1] = P[K-1];

      for (i = 0; i <= K-2; i = i + 1)begin
        assign SET_CMD[i] = SET_CMD[i+1] | G[i];
      end

      for (i = 0; i <= K-1; i = i + 1)begin
        assign OUT[i] = SET_CMD[i] | P[i];
      end

    end
  endgenerate
endmodule // eta1
