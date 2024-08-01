// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
//- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
module LOBA0s
    # (parameter N=16, parameter K=4)
    (a, b, r);

    input [N-1:0] a;
    input [N-1:0] b;
    output [2*N-1:0] r;

    wire [N-1:0] a_temp;
    wire [N-1:0] b_temp;
    wire [2*N-1:0] r_temp;
    wire out_sign;

    LOBA0u #(.N(N), .K(K)) u1 (.a(a_temp), .b(b_temp), .r(r_temp));

    assign a_temp = a[N-1] ? ~a + 1 : a;
    assign b_temp = b[N-1] ? ~b + 1 : b;
    assign out_sign = a[N-1] ^ b[N-1];
    assign r = out_sign ? ~ r_temp + 1 : r_temp;

endmodule


module LOBA0u
    # (parameter N=16, parameter K=4)
    (a, b, r);

    input [N-1:0] a;
    input [N-1:0] b;
    output [2*N-1:0] r;

    wire [K-1:0] Ah;
    wire [K-1:0] Al;
    wire [$clog2(N)-1:0] k1a;
    wire [$clog2(N)-1:0] k2a;

    wire [K-1:0] Bh;
    wire [K-1:0] Bl;
    wire [$clog2(N)-1:0] k1b;
    wire [$clog2(N)-1:0] k2b;

    LOBA_SPLIT #(.N(N),.K(K)) u1 (.X(a), .Xh(Ah), .kh(k1a), .Xl(Al), .kl(k2a));
    LOBA_SPLIT #(.N(N),.K(K)) u2 (.X(b), .Xh(Bh), .kh(k1b), .Xl(Bl), .kl(k2b));

    assign r =
        ((Ah*Bh)<<(k1a+k1b-(2*(K-1))))
        ;
endmodule

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
//- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

module LOBA1s
    # (parameter N=16, parameter K=4)
    (a, b, r);

    input [N-1:0] a;
    input [N-1:0] b;
    output [2*N-1:0] r;

    wire [N-1:0] a_temp;
    wire [N-1:0] b_temp;
    wire [2*N-1:0] r_temp;
    wire out_sign;

    LOBA1u #(.N(N), .K(K)) u1 (.a(a_temp), .b(b_temp), .r(r_temp));

    assign a_temp = a[N-1] ? ~a + 1 : a;
    assign b_temp = b[N-1] ? ~b + 1 : b;
    assign out_sign = a[N-1] ^ b[N-1];
    assign r = out_sign ? ~ r_temp + 1 : r_temp;

endmodule


module LOBA1u
    # (parameter N=16, parameter K=4)
    (a, b, r);

    input [N-1:0] a;
    input [N-1:0] b;
    output [2*N-1:0] r;

    wire [K-1:0] Ah;
    wire [K-1:0] Al;
    wire [$clog2(N)-1:0] k1a;
    wire [$clog2(N)-1:0] k2a;

    wire [K-1:0] Bh;
    wire [K-1:0] Bl;
    wire [$clog2(N)-1:0] k1b;
    wire [$clog2(N)-1:0] k2b;

    LOBA_SPLIT #(.N(N),.K(K)) u1 (.X(a), .Xh(Ah), .kh(k1a), .Xl(Al), .kl(k2a));
    LOBA_SPLIT #(.N(N),.K(K)) u2 (.X(b), .Xh(Bh), .kh(k1b), .Xl(Bl), .kl(k2b));

    assign r =
        ((Ah*Bh)<<(k1a+k1b-(2*(K-1))))
        +
        ((Ah*Bl)<<(k1a+k2b-(2*(K-1))))
        ;
endmodule

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
//- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

module LOBA2s
    # (parameter N=16, parameter K=4)
    (a, b, r);

    input [N-1:0] a;
    input [N-1:0] b;
    output [2*N-1:0] r;

    wire [N-1:0] a_temp;
    wire [N-1:0] b_temp;
    wire [2*N-1:0] r_temp;
    wire out_sign;

    LOBA2u #(.N(N), .K(K)) u1 (.a(a_temp), .b(b_temp), .r(r_temp));

    assign a_temp = a[N-1] ? ~a + 1 : a;
    assign b_temp = b[N-1] ? ~b + 1 : b;
    assign out_sign = a[N-1] ^ b[N-1];
    assign r = out_sign ? ~ r_temp + 1 : r_temp;

endmodule


module LOBA2u
    # (parameter N=16, parameter K=4)
    (a, b, r);

    input [N-1:0] a;
    input [N-1:0] b;
    output [2*N-1:0] r;

    wire [K-1:0] Ah;
    wire [K-1:0] Al;
    wire [$clog2(N)-1:0] k1a;
    wire [$clog2(N)-1:0] k2a;

    wire [K-1:0] Bh;
    wire [K-1:0] Bl;
    wire [$clog2(N)-1:0] k1b;
    wire [$clog2(N)-1:0] k2b;

    LOBA_SPLIT #(.N(N),.K(K)) u1 (.X(a), .Xh(Ah), .kh(k1a), .Xl(Al), .kl(k2a));
    LOBA_SPLIT #(.N(N),.K(K)) u2 (.X(b), .Xh(Bh), .kh(k1b), .Xl(Bl), .kl(k2b));

    assign r =
        ((Ah*Bh)<<(k1a+k1b-(2*(K-1))))
        +
        ((Ah*Bl)<<(k1a+k2b-(2*(K-1))))
        +
        ((Al*Bh)<<(k2a+k1b-(2*(K-1))))
        ;
endmodule

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
//- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

module LOBA3s
    # (parameter N=16, parameter K=4)
    (a, b, r);

    input [N-1:0] a;
    input [N-1:0] b;
    output [2*N-1:0] r;

    wire [N-1:0] a_temp;
    wire [N-1:0] b_temp;
    wire [2*N-1:0] r_temp;
    wire out_sign;

    LOBA3u #(.N(N), .K(K)) u1 (.a(a_temp), .b(b_temp), .r(r_temp));

    assign a_temp = a[N-1] ? ~a + 1 : a;
    assign b_temp = b[N-1] ? ~b + 1 : b;
    assign out_sign = a[N-1] ^ b[N-1];
    assign r = out_sign ? ~ r_temp + 1 : r_temp;

endmodule


module LOBA3u
    # (parameter N=16, parameter K=4)
    (a, b, r);

    input [N-1:0] a;
    input [N-1:0] b;
    output [2*N-1:0] r;

    wire [K-1:0] Ah;
    wire [K-1:0] Al;
    wire [$clog2(N)-1:0] k1a;
    wire [$clog2(N)-1:0] k2a;

    wire [K-1:0] Bh;
    wire [K-1:0] Bl;
    wire [$clog2(N)-1:0] k1b;
    wire [$clog2(N)-1:0] k2b;

    LOBA_SPLIT #(.N(N),.K(K)) u1 (.X(a), .Xh(Ah), .kh(k1a), .Xl(Al), .kl(k2a));
    LOBA_SPLIT #(.N(N),.K(K)) u2 (.X(b), .Xh(Bh), .kh(k1b), .Xl(Bl), .kl(k2b));

    assign r =
        ((Ah*Bh)<<(k1a+k1b-(2*(K-1))))
        +
        ((Ah*Bl)<<(k1a+k2b-(2*(K-1))))
        +
        ((Al*Bh)<<(k2a+k1b-(2*(K-1))))
        +
        ((Al*Bl)<<(k2a+k2b-(2*(K-1))))
        ;
endmodule

// - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
//- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

module LOBA_SPLIT
    # (parameter N=16, parameter K=4)
    (X, Xh, Xl, kh, kl);

    input [N-1:0] X;
    output reg [K-1:0] Xh;
    output reg [K-1:0] Xl;
    output reg [$clog2(N)-1:0] kh;
    output reg [$clog2(N)-1:0] kl;

    wire [N-1:0] lobh;
    wire [N-1:0] lobl;
    reg [N-1:0] lower;
    genvar i;

    LOBA_LOB #(.N(N)) u1 (.x(X), .y(lobh));
    LOBA_LOB #(.N(N)) u2 (.x(lower), .y(lobl));

    LOBA_MUX #(.K(K), .N(N)) u3 (.in_a(X), .select(kh), .out(Xh));
    LOBA_MUX #(.K(K), .N(N)) u4 (.in_a(X), .select(kl), .out(Xl));

    LOBA_LOWER #(.N(N)) u5 (.in_a(X), .select(kh-K), .out(lower));

    generate
        for (i=N-1; i>=K-1; i=i-1) begin
            always @ (*) begin
                if (lobh[i] == 1) begin
                    kh <= i;
                end

                if (lobl[i] == 1) begin
                    kl <= i;
                end
            end
        end
    endgenerate
endmodule


module LOBA_MUX
    # (parameter N=16, parameter K=4)
    (in_a, select, out);

    input [$clog2(N)-1:0] select;
    input [N-1:0] in_a;
    output reg [K-1:0] out;
    integer i;

    always @ (*) begin
        out = 0;
        for (i=K-1; i<(N); i=i+1) begin
            if (select == i) begin
                out <= in_a[i -: K];
            end
        end
    end

endmodule


module LOBA_LOWER
    #(parameter N=16)
    (in_a, select, out);

    input [$clog2(N)-1:0] select;
    input [N-1:0] in_a;
    output reg [N-1:0] out;
    genvar i;

    for (i=N-1; i>=0; i=i-1) begin
        always @ (*) begin
            if (select == i) begin
                out[N-1:i] <= 0;
                out[i:0] <= in_a[i:0];
            end
        end
    end

endmodule


module LOBA_LOB
    # (parameter N=16)
    (x, y);
    input [N-1:0] x;
    output reg [N-1:0] y;
    integer k;
    reg [N-1:0]w;
    always @ (*) begin
        y[N-1]=x[N-1];
        w[N-1]=x[N-1]?0:1;
        for (k=N-2;k>=0;k=k-1) begin
            w[k]=x[k]?0:w[k+1];
            y[k]=w[k+1]&x[k];
        end
    end
endmodule





