/*
Copyright (c) 2015 Soheil Hashemi (soheil_hashemi@brown.edu)
              2018 German Research Center for Artificial Intelligence (DFKI)

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

Approximate Multiplier Design Details Provided in:
Soheil Hashemi, R. Iris Bahar, and Sherief Reda, "DRUM: A Dynamic
Range Unbiased Multiplier for Approximate Applications" In
Proceedings of the IEEE/ACM International Conference on
Computer-Aided Design (ICCAD). 2015. 

*/

module DRUMs
    # (parameter N=16, parameter K=4)
    (a, b, r);

    input [N-1:0] a;
    input [N-1:0] b;
    output [2*N-1:0] r;

    wire [N-1:0] a_temp;
    wire [N-1:0] b_temp;
    wire [2*N-1:0] r_temp;
    wire out_sign;

    DRUMu #(.N(N), .K(K)) U1 (.a(a_temp), .b(b_temp), .r(r_temp));

    assign a_temp = a[N-1] ? ~a + 1 : a;
    assign b_temp = b[N-1] ? ~b + 1 : b;
    assign out_sign = a[N-1] ^ b[N-1];
    assign r = out_sign ? ~ r_temp + 1 : r_temp;

endmodule

module DRUMu
    # (parameter N=16, parameter K=6)
    (a, b, r);

    input [N-1:0] a;
    input [N-1:0] b;
    output [2*N-1:0] r;

    wire [$clog2(N)-1:0] k1;
    wire [$clog2(N)-1:0] k2;
    wire [K-3:0] m;
    wire [K-3:0] n;
    wire [N-1:0] l1;
    wire [N-1:0] l2;
    wire [(K*2)-1:0] tmp;
    wire [$clog2(N)-1:0] p;
    wire [$clog2(N)-1:0] q;
    wire [$clog2(N):0]sum;
    wire [K-1:0] mm;
    wire [K-1:0] nn;

    DRUM_LOD_k #(.N(N)) u1 (.in_a(a), .out_a(l1));
    DRUM_LOD_k #(.N(N)) u2 (.in_a(b), .out_a(l2));

    DRUM_P_Encoder_k #(.N(N)) u3 (.in_a(l1), .out_a(k1));
    DRUM_P_Encoder_k #(.N(N)) u4 (.in_a(l2), .out_a(k2));

    DRUM_Mux_16_3_k #(.N(N), .K(K)) u5 (.in_a(a), .select(k1), .out(n));
    DRUM_Mux_16_3_k #(.N(N), .K(K)) u6 (.in_a(b), .select(k2), .out(m));

    DRUM_Barrel_Shifter_k #(.K(K), .N(N)) u7 (.in_a(tmp), .count(sum), .out_a(r));

    assign p = k1 > (K-1) ? k1 - (K-1) : 0;
    assign q = k2 > (K-1) ? k2 - (K-1) : 0;
    assign mm = k1 > (K-1) ? {1'b1, n, 1'b1} : a[K-1:0];
    assign nn = k2 > (K-1) ? {1'b1, m, 1'b1} : b[K-1:0];
    assign tmp = mm * nn;
    assign sum = p + q;

endmodule


module DRUM_LOD_k
    # (parameter N=16)
    (in_a, out_a);

    input [N-1:0]in_a;
    output reg [N-1:0]out_a;
    integer k,j;
    reg [N-1:0]w;

    always @ (*) begin
        out_a[N-1]=in_a[N-1];
        w[N-1]=in_a[N-1]?0:1;
        for (k=N-2;k>=0;k=k-1)
            begin
            w[k]=in_a[k]?0:w[k+1];
            out_a[k]=w[k+1]&in_a[k];
            end
    end

endmodule


module DRUM_P_Encoder_k
    # (parameter N=16)
    (in_a, out_a);

    input [N-1:0]in_a;
    output reg [$clog2(N)-1:0]out_a;
    integer i;

    always @ (*) begin
        out_a = 0;
        for (i=N-1; i>=0; i=i-1)
            if (in_a[i]) out_a = i[$clog2(N)-1:0];
    end

endmodule


module DRUM_Barrel_Shifter_k
    # (parameter N=16, parameter K=6)
    (in_a, count, out_a);

    input [$clog2(N):0]count;
    input [(K*2)-1:0]in_a;
    output [2*N-1:0]out_a;
    wire [2*N-1:0] tmp;

    assign tmp = {{((2*N)-(K*2)){1'b0}}, in_a};
    assign out_a=(tmp<<count);

endmodule


module DRUM_Mux_16_3_k
    #(parameter N=16, parameter K=6)
    (in_a, select, out);

    input [$clog2(N)-1:0]select;
    input [N-1:0]in_a;
    output reg [K-3:0]out;
    integer i;

    always @(*) begin
        out = 0;
        for (i = K;i<(N);i=i+1) begin :mux_gen_block
            if (select == i[$clog2(N)-1:0])
                out = in_a[i-1 -: K-2];
        end
    end

endmodule
