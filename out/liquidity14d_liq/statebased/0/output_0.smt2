; benchmark generated from python API
(set-info :status unknown)
(declare-datatypes ((Proc 0)) (((pay) (unlock))))
 (declare-fun w_0 () Int)
(declare-fun b_1 () Bool)
(declare-fun t_b_0_0 () Bool)
(declare-fun aw_0_2 () Int)
(declare-fun aw_1_2 () Int)
(declare-fun aw_0_1 () Int)
(declare-fun aw_1_1 () Int)
(declare-fun aw_0_0 () Int)
(declare-fun aw_1_0 () Int)
(declare-fun w_1 () Int)
(declare-fun b_0 () Bool)
(declare-fun xn_0 () Int)
(declare-fun xa_0 () Int)
(declare-fun b_2 () Bool)
(declare-fun t_b_1_0 () Bool)
(declare-fun t_aw_1_0_2 () Int)
(declare-fun aw_2_2 () Int)
(declare-fun t_aw_1_0_1 () Int)
(declare-fun aw_2_1 () Int)
(declare-fun t_aw_1_0_0 () Int)
(declare-fun aw_2_0 () Int)
(declare-fun t_w_1_0 () Int)
(declare-fun w_2 () Int)
(declare-fun pay_amount_1 () Int)
(declare-fun xa_1 () Int)
(declare-fun xn_1 () Int)
(declare-fun f_1 () Proc)
(declare-fun block_num_1 () Int)
(declare-fun block_num_2 () Int)
(assert
 (>= w_0 0))
(assert
 (let (($x119 (= t_b_0_0 b_1)))
 (let (($x115 (= aw_1_2 aw_0_2)))
 (let (($x114 (= aw_1_1 aw_0_1)))
 (let (($x113 (= aw_1_0 aw_0_0)))
 (let (($x116 (and $x113 $x114 $x115)))
 (let (($x112 (= w_1 w_0)))
 (let (($x120 (and $x112 $x116 $x119)))
 (let (($x123 (ite (not (= xn_0 0)) (and $x112 $x116 (= b_0 b_1)) (and (and true $x120) true $x120))))
 (and (and (>= xa_0 0) (<= xa_0 2) (>= xn_0 0)) (and (>= aw_0_0 0) (>= aw_0_1 0) (>= aw_0_2 0)) $x123))))))))))
(assert
 (let (($x150 (= t_b_1_0 b_2)))
 (let (($x186 (= aw_2_2 t_aw_1_0_2)))
 (let (($x185 (= aw_2_1 t_aw_1_0_1)))
 (let (($x184 (= aw_2_0 t_aw_1_0_0)))
 (let (($x183 (= w_2 t_w_1_0)))
 (let (($x188 (and $x183 (and $x184 $x185 $x186) $x150)))
 (let (($x179 (= t_aw_1_0_2 aw_1_2)))
 (let (($x176 (= xa_1 2)))
 (let (($x174 (= t_aw_1_0_1 aw_1_1)))
 (let (($x171 (= xa_1 1)))
 (let (($x168 (= t_aw_1_0_0 aw_1_0)))
 (let (($x165 (= xa_1 0)))
 (let (($x181 (and (ite $x165 (= t_aw_1_0_0 (+ aw_1_0 pay_amount_1)) $x168) (ite $x171 (= t_aw_1_0_1 (+ aw_1_1 pay_amount_1)) $x174) (ite $x176 (= t_aw_1_0_2 (+ aw_1_2 pay_amount_1)) $x179))))
 (let (($x145 (= b_1 b_2)))
 (let (($x143 (= aw_2_2 aw_1_2)))
 (let (($x142 (= aw_2_1 aw_1_1)))
 (let (($x141 (= aw_2_0 aw_1_0)))
 (let (($x144 (and $x141 $x142 $x143)))
 (let (($x140 (= w_2 w_1)))
 (let (($x146 (and $x140 $x144 $x145)))
 (let (($x190 (ite (not (>= pay_amount_1 0)) $x146 (and (and (= t_w_1_0 (- w_1 pay_amount_1)) $x181) true $x188))))
 (let (($x194 (ite (not (and (<= pay_amount_1 w_1) b_1)) $x146 (and (and (and (= t_b_1_0 false) $x190) true $x188)))))
 (let (($x138 (= xn_1 0)))
 (let (($x139 (not $x138)))
 (let (($x147 (not b_1)))
 (let (($x148 (not $x147)))
 (let (($x154 (ite $x148 $x146 (and (and (= t_b_1_0 true) true (and $x140 $x144 $x150))))))
 (let (($x137 (= f_1 unlock)))
 (let (($x134 (>= aw_1_2 0)))
 (let (($x133 (>= aw_1_1 0)))
 (let (($x132 (>= aw_1_0 0)))
 (let (($x135 (and $x132 $x133 $x134)))
 (and (and (>= xa_1 0) (<= xa_1 2) (>= xn_1 0)) $x135 (>= block_num_2 block_num_1) (ite $x137 (ite $x139 $x146 (and $x154)) (ite $x139 $x146 (and $x194)))))))))))))))))))))))))))))))))))))
(assert
 (let (($x567 (exists ((xa_q Int) )(let (($x271 (forall ((xn_q0 Int) (f_q0 Proc) (wq0 Int) (awq0_0 Int) (awq0_1 Int) (awq0_2 Int) (t_wq0_0 Int) (t_awq0_0_0 Int) (t_awq0_0_1 Int) (t_awq0_0_2 Int) (block_num_q0 Int) (pay_amount0_q Int) (bq0 Bool) (t_bq0_0 Bool) )(let (($x245 (and (or (and (distinct xa_q 0) true) (not (= awq0_0 (+ aw_1_0 w_1)))) (or (and (distinct xa_q 1) true) (not (= awq0_1 (+ aw_1_1 w_1)))) (or (and (distinct xa_q 2) true) (not (= awq0_2 (+ aw_1_2 w_1)))))))
 (let (($x340 (= t_bq0_0 bq0)))
 (let (($x345 (= wq0 t_wq0_0)))
 (let (($x346 (and $x345 (and (= awq0_0 t_awq0_0_0) (= awq0_1 t_awq0_0_1) (= awq0_2 t_awq0_0_2)) $x340)))
 (let (($x252 (and (ite (= xa_q 0) (= t_awq0_0_0 (+ aw_1_0 pay_amount0_q)) (= t_awq0_0_0 aw_1_0)) (ite (= xa_q 1) (= t_awq0_0_1 (+ aw_1_1 pay_amount0_q)) (= t_awq0_0_1 aw_1_1)) (ite (= xa_q 2) (= t_awq0_0_2 (+ aw_1_2 pay_amount0_q)) (= t_awq0_0_2 aw_1_2)))))
 (let (($x364 (= b_1 bq0)))
 (let (($x365 (= awq0_2 aw_1_2)))
 (let (($x366 (= awq0_1 aw_1_1)))
 (let (($x367 (= awq0_0 aw_1_0)))
 (let (($x368 (and $x367 $x366 $x365)))
 (let (($x369 (= wq0 w_1)))
 (let (($x370 (and $x369 $x368 $x364)))
 (let (($x371 (>= pay_amount0_q 0)))
 (let (($x372 (not $x371)))
 (let (($x374 (= t_bq0_0 false)))
 (let (($x256 (and $x374 (ite $x372 $x370 (and (and (= t_wq0_0 (- w_1 pay_amount0_q)) $x252) true $x346)))))
 (let (($x259 (ite (not (and (<= pay_amount0_q w_1) b_1)) $x370 (and (and $x256 true $x346)))))
 (let (($x383 (= xn_q0 0)))
 (let (($x384 (not $x383)))
 (let (($x147 (not b_1)))
 (let (($x148 (not $x147)))
 (let (($x390 (ite $x148 $x370 (and (and (= t_bq0_0 true) true (and $x369 $x368 $x340))))))
 (let (($x393 (= f_q0 unlock)))
 (let (($x134 (>= aw_1_2 0)))
 (let (($x133 (>= aw_1_1 0)))
 (let (($x132 (>= aw_1_0 0)))
 (let (($x135 (and $x132 $x133 $x134)))
 (let (($x267 (and (and (>= xa_q 0) (<= xa_q 2) (>= xn_q0 0)) $x135 (>= block_num_q0 block_num_1) (ite $x393 (ite $x384 $x370 (and $x390)) (ite $x384 $x370 (and $x259))))))
 (or (not $x267) $x245))))))))))))))))))))))))))))))
 ))
 (let (($x278 (= b_1 true)))
 (let (($x272 (<= xa_q 2)))
 (let (($x273 (>= xa_q 0)))
 (let (($x274 (and $x273 $x272)))
 (and $x274 $x278 $x271)))))))
 ))
 (and $x567)))
(check-sat)
