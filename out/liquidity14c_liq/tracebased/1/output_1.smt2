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
(declare-fun b_3 () Bool)
(declare-fun t_b_2_0 () Bool)
(declare-fun t_aw_2_0_2 () Int)
(declare-fun aw_3_2 () Int)
(declare-fun t_aw_2_0_1 () Int)
(declare-fun aw_3_1 () Int)
(declare-fun t_aw_2_0_0 () Int)
(declare-fun aw_3_0 () Int)
(declare-fun t_w_2_0 () Int)
(declare-fun w_3 () Int)
(declare-fun pay_amount_2 () Int)
(declare-fun xa_2 () Int)
(declare-fun xn_2 () Int)
(declare-fun f_2 () Proc)
(declare-fun block_num_3 () Int)
(declare-fun b_4 () Bool)
(declare-fun t_b_3_0 () Bool)
(declare-fun t_aw_3_0_2 () Int)
(declare-fun aw_4_2 () Int)
(declare-fun t_aw_3_0_1 () Int)
(declare-fun aw_4_1 () Int)
(declare-fun t_aw_3_0_0 () Int)
(declare-fun aw_4_0 () Int)
(declare-fun t_w_3_0 () Int)
(declare-fun w_4 () Int)
(declare-fun pay_amount_3 () Int)
(declare-fun xa_3 () Int)
(declare-fun xn_3 () Int)
(declare-fun f_3 () Proc)
(declare-fun block_num_4 () Int)
(assert
 (>= w_0 0))
(assert
 (let (($x150 (= t_b_0_0 b_1)))
 (let (($x145 (= aw_1_2 aw_0_2)))
 (let (($x144 (= aw_1_1 aw_0_1)))
 (let (($x143 (= aw_1_0 aw_0_0)))
 (let (($x146 (and $x143 $x144 $x145)))
 (let (($x142 (= w_1 w_0)))
 (let (($x151 (and $x142 $x146 $x150)))
 (let (($x154 (ite (not (= xn_0 0)) (and $x142 $x146 (= b_0 b_1)) (and (and (= t_b_0_0 false) $x151) true $x151))))
 (and (and (>= xa_0 0) (<= xa_0 2) (>= xn_0 0)) (and (>= aw_0_0 0) (>= aw_0_1 0) (>= aw_0_2 0)) $x154))))))))))
(assert
 (let (($x183 (= t_b_1_0 b_2)))
 (let (($x219 (= aw_2_2 t_aw_1_0_2)))
 (let (($x218 (= aw_2_1 t_aw_1_0_1)))
 (let (($x217 (= aw_2_0 t_aw_1_0_0)))
 (let (($x216 (= w_2 t_w_1_0)))
 (let (($x221 (and $x216 (and $x217 $x218 $x219) $x183)))
 (let (($x212 (= t_aw_1_0_2 aw_1_2)))
 (let (($x209 (= xa_1 2)))
 (let (($x207 (= t_aw_1_0_1 aw_1_1)))
 (let (($x204 (= xa_1 1)))
 (let (($x201 (= t_aw_1_0_0 aw_1_0)))
 (let (($x198 (= xa_1 0)))
 (let (($x214 (and (ite $x198 (= t_aw_1_0_0 (+ aw_1_0 pay_amount_1)) $x201) (ite $x204 (= t_aw_1_0_1 (+ aw_1_1 pay_amount_1)) $x207) (ite $x209 (= t_aw_1_0_2 (+ aw_1_2 pay_amount_1)) $x212))))
 (let (($x178 (= b_1 b_2)))
 (let (($x176 (= aw_2_2 aw_1_2)))
 (let (($x175 (= aw_2_1 aw_1_1)))
 (let (($x174 (= aw_2_0 aw_1_0)))
 (let (($x177 (and $x174 $x175 $x176)))
 (let (($x173 (= w_2 w_1)))
 (let (($x179 (and $x173 $x177 $x178)))
 (let (($x223 (ite (not (>= pay_amount_1 0)) $x179 (and (and (= t_w_1_0 (- w_1 pay_amount_1)) $x214) true $x221))))
 (let (($x227 (ite (not (and (<= pay_amount_1 w_1) b_1)) $x179 (and (and (and (= t_b_1_0 false) $x223) true $x221)))))
 (let (($x171 (= xn_1 0)))
 (let (($x172 (not $x171)))
 (let (($x180 (not b_1)))
 (let (($x181 (not $x180)))
 (let (($x187 (ite $x181 $x179 (and (and (= t_b_1_0 true) true (and $x173 $x177 $x183))))))
 (let (($x170 (= f_1 unlock)))
 (let (($x167 (>= aw_1_2 0)))
 (let (($x166 (>= aw_1_1 0)))
 (let (($x165 (>= aw_1_0 0)))
 (let (($x168 (and $x165 $x166 $x167)))
 (and (and (>= xa_1 0) (<= xa_1 2) (>= xn_1 0)) $x168 (>= block_num_2 block_num_1) (ite $x170 (ite $x172 $x179 (and $x187)) (ite $x172 $x179 (and $x227)))))))))))))))))))))))))))))))))))))
(assert
 (let (($x288 (= t_b_2_0 b_3)))
 (let (($x323 (= aw_3_2 t_aw_2_0_2)))
 (let (($x322 (= aw_3_1 t_aw_2_0_1)))
 (let (($x321 (= aw_3_0 t_aw_2_0_0)))
 (let (($x320 (= w_3 t_w_2_0)))
 (let (($x325 (and $x320 (and $x321 $x322 $x323) $x288)))
 (let (($x316 (= t_aw_2_0_2 aw_2_2)))
 (let (($x313 (= xa_2 2)))
 (let (($x311 (= t_aw_2_0_1 aw_2_1)))
 (let (($x308 (= xa_2 1)))
 (let (($x306 (= t_aw_2_0_0 aw_2_0)))
 (let (($x303 (= xa_2 0)))
 (let (($x318 (and (ite $x303 (= t_aw_2_0_0 (+ aw_2_0 pay_amount_2)) $x306) (ite $x308 (= t_aw_2_0_1 (+ aw_2_1 pay_amount_2)) $x311) (ite $x313 (= t_aw_2_0_2 (+ aw_2_2 pay_amount_2)) $x316))))
 (let (($x283 (= b_2 b_3)))
 (let (($x281 (= aw_3_2 aw_2_2)))
 (let (($x280 (= aw_3_1 aw_2_1)))
 (let (($x279 (= aw_3_0 aw_2_0)))
 (let (($x282 (and $x279 $x280 $x281)))
 (let (($x278 (= w_3 w_2)))
 (let (($x284 (and $x278 $x282 $x283)))
 (let (($x327 (ite (not (>= pay_amount_2 0)) $x284 (and (and (= t_w_2_0 (- w_2 pay_amount_2)) $x318) true $x325))))
 (let (($x331 (ite (not (and (<= pay_amount_2 w_2) b_2)) $x284 (and (and (and (= t_b_2_0 false) $x327) true $x325)))))
 (let (($x276 (= xn_2 0)))
 (let (($x277 (not $x276)))
 (let (($x285 (not b_2)))
 (let (($x286 (not $x285)))
 (let (($x292 (ite $x286 $x284 (and (and (= t_b_2_0 true) true (and $x278 $x282 $x288))))))
 (let (($x275 (= f_2 unlock)))
 (let (($x272 (>= aw_2_2 0)))
 (let (($x271 (>= aw_2_1 0)))
 (let (($x270 (>= aw_2_0 0)))
 (let (($x273 (and $x270 $x271 $x272)))
 (and (and (>= xa_2 0) (<= xa_2 2) (>= xn_2 0)) $x273 (>= block_num_3 block_num_2) (ite $x275 (ite $x277 $x284 (and $x292)) (ite $x277 $x284 (and $x331)))))))))))))))))))))))))))))))))))))
(assert
 (let (($x391 (= t_b_3_0 b_4)))
 (let (($x426 (= aw_4_2 t_aw_3_0_2)))
 (let (($x425 (= aw_4_1 t_aw_3_0_1)))
 (let (($x424 (= aw_4_0 t_aw_3_0_0)))
 (let (($x423 (= w_4 t_w_3_0)))
 (let (($x428 (and $x423 (and $x424 $x425 $x426) $x391)))
 (let (($x419 (= t_aw_3_0_2 aw_3_2)))
 (let (($x416 (= xa_3 2)))
 (let (($x414 (= t_aw_3_0_1 aw_3_1)))
 (let (($x411 (= xa_3 1)))
 (let (($x409 (= t_aw_3_0_0 aw_3_0)))
 (let (($x406 (= xa_3 0)))
 (let (($x421 (and (ite $x406 (= t_aw_3_0_0 (+ aw_3_0 pay_amount_3)) $x409) (ite $x411 (= t_aw_3_0_1 (+ aw_3_1 pay_amount_3)) $x414) (ite $x416 (= t_aw_3_0_2 (+ aw_3_2 pay_amount_3)) $x419))))
 (let (($x386 (= b_3 b_4)))
 (let (($x384 (= aw_4_2 aw_3_2)))
 (let (($x383 (= aw_4_1 aw_3_1)))
 (let (($x382 (= aw_4_0 aw_3_0)))
 (let (($x385 (and $x382 $x383 $x384)))
 (let (($x381 (= w_4 w_3)))
 (let (($x387 (and $x381 $x385 $x386)))
 (let (($x430 (ite (not (>= pay_amount_3 0)) $x387 (and (and (= t_w_3_0 (- w_3 pay_amount_3)) $x421) true $x428))))
 (let (($x434 (ite (not (and (<= pay_amount_3 w_3) b_3)) $x387 (and (and (and (= t_b_3_0 false) $x430) true $x428)))))
 (let (($x379 (= xn_3 0)))
 (let (($x380 (not $x379)))
 (let (($x388 (not b_3)))
 (let (($x389 (not $x388)))
 (let (($x395 (ite $x389 $x387 (and (and (= t_b_3_0 true) true (and $x381 $x385 $x391))))))
 (let (($x378 (= f_3 unlock)))
 (let (($x375 (>= aw_3_2 0)))
 (let (($x374 (>= aw_3_1 0)))
 (let (($x373 (>= aw_3_0 0)))
 (let (($x376 (and $x373 $x374 $x375)))
 (and (and (>= xa_3 0) (<= xa_3 2) (>= xn_3 0)) $x376 (>= block_num_4 block_num_3) (ite $x378 (ite $x380 $x387 (and $x395)) (ite $x380 $x387 (and $x434)))))))))))))))))))))))))))))))))))))
(assert
 (let (($x671 (exists ((xa_q Int) )(let (($x674 (forall ((xn_q0 Int) (f_q0 Proc) (wq0 Int) (awq0_0 Int) (awq0_1 Int) (awq0_2 Int) (t_wq0_0 Int) (t_awq0_0_0 Int) (t_awq0_0_1 Int) (t_awq0_0_2 Int) (block_num_q0 Int) (pay_amount0_q Int) (bq0 Bool) (t_bq0_0 Bool) (xn_q1 Int) (f_q1 Proc) (wq1 Int) (awq1_0 Int) (awq1_1 Int) (awq1_2 Int) (t_wq1_0 Int) (t_awq1_0_0 Int) (t_awq1_0_1 Int) (t_awq1_0_2 Int) (block_num_q1 Int) (pay_amount1_q Int) (bq1 Bool) (t_bq1_0 Bool) )(let (($x738 (and (or (and (distinct xa_q 0) true) (not (= awq1_0 (+ aw_2_0 w_2)))) (or (and (distinct xa_q 1) true) (not (= awq1_1 (+ aw_2_1 w_2)))) (or (and (distinct xa_q 2) true) (not (= awq1_2 (+ aw_2_2 w_2)))))))
 (let (($x579 (= t_bq1_0 bq1)))
 (let (($x584 (= wq1 t_wq1_0)))
 (let (($x585 (and $x584 (and (= awq1_0 t_awq1_0_0) (= awq1_1 t_awq1_0_1) (= awq1_2 t_awq1_0_2)) $x579)))
 (let (($x624 (and (ite (= xa_q 0) (= t_awq1_0_0 (+ awq0_0 pay_amount1_q)) (= t_awq1_0_0 awq0_0)) (ite (= xa_q 1) (= t_awq1_0_1 (+ awq0_1 pay_amount1_q)) (= t_awq1_0_1 awq0_1)) (ite (= xa_q 2) (= t_awq1_0_2 (+ awq0_2 pay_amount1_q)) (= t_awq1_0_2 awq0_2)))))
 (let (($x758 (= bq0 bq1)))
 (let (($x759 (= awq1_2 awq0_2)))
 (let (($x760 (= awq1_1 awq0_1)))
 (let (($x761 (= awq1_0 awq0_0)))
 (let (($x762 (and $x761 $x760 $x759)))
 (let (($x763 (= wq1 wq0)))
 (let (($x764 (and $x763 $x762 $x758)))
 (let (($x610 (>= pay_amount1_q 0)))
 (let (($x611 (not $x610)))
 (let (($x613 (= t_bq1_0 false)))
 (let (($x538 (and $x613 (ite $x611 $x764 (and (and (= t_wq1_0 (- wq0 pay_amount1_q)) $x624) true $x585)))))
 (let (($x574 (ite (not (and (<= pay_amount1_q wq0) bq0)) $x764 (and (and $x538 true $x585)))))
 (let (($x622 (= xn_q1 0)))
 (let (($x623 (not $x622)))
 (let (($x780 (ite (not (not bq0)) $x764 (and (and (= t_bq1_0 true) true (and $x763 $x762 $x579))))))
 (let (($x632 (= f_q1 unlock)))
 (let (($x518 (and (and (>= xa_q 0) (<= xa_q 2) (>= xn_q1 0)) (and (>= awq0_0 0) (>= awq0_1 0) (>= awq0_2 0)) (>= block_num_q1 block_num_q0) (ite $x632 (ite $x623 $x764 (and $x780)) (ite $x623 $x764 (and $x574))))))
 (let (($x519 (not $x518)))
 (let (($x792 (= t_bq0_0 bq0)))
 (let (($x797 (= wq0 t_wq0_0)))
 (let (($x798 (and $x797 (and (= awq0_0 t_awq0_0_0) (= awq0_1 t_awq0_0_1) (= awq0_2 t_awq0_0_2)) $x792)))
 (let (($x695 (and (ite (= xa_q 0) (= t_awq0_0_0 (+ aw_2_0 pay_amount0_q)) (= t_awq0_0_0 aw_2_0)) (ite (= xa_q 1) (= t_awq0_0_1 (+ aw_2_1 pay_amount0_q)) (= t_awq0_0_1 aw_2_1)) (ite (= xa_q 2) (= t_awq0_0_2 (+ aw_2_2 pay_amount0_q)) (= t_awq0_0_2 aw_2_2)))))
 (let (($x966 (= b_2 bq0)))
 (let (($x967 (= awq0_2 aw_2_2)))
 (let (($x968 (= awq0_1 aw_2_1)))
 (let (($x969 (= awq0_0 aw_2_0)))
 (let (($x970 (and $x969 $x968 $x967)))
 (let (($x971 (= wq0 w_2)))
 (let (($x972 (and $x971 $x970 $x966)))
 (let (($x823 (>= pay_amount0_q 0)))
 (let (($x824 (not $x823)))
 (let (($x826 (= t_bq0_0 false)))
 (let (($x706 (and $x826 (ite $x824 $x972 (and (and (= t_wq0_0 (- w_2 pay_amount0_q)) $x695) true $x798)))))
 (let (($x714 (ite (not (and (<= pay_amount0_q w_2) b_2)) $x972 (and (and $x706 true $x798)))))
 (let (($x835 (= xn_q0 0)))
 (let (($x836 (not $x835)))
 (let (($x285 (not b_2)))
 (let (($x286 (not $x285)))
 (let (($x986 (ite $x286 $x972 (and (and (= t_bq0_0 true) true (and $x971 $x970 $x792))))))
 (let (($x845 (= f_q0 unlock)))
 (let (($x272 (>= aw_2_2 0)))
 (let (($x271 (>= aw_2_1 0)))
 (let (($x270 (>= aw_2_0 0)))
 (let (($x273 (and $x270 $x271 $x272)))
 (let (($x848 (>= xn_q0 0)))
 (let (($x639 (<= xa_q 2)))
 (let (($x640 (>= xa_q 0)))
 (let (($x536 (and $x640 $x639 $x848)))
 (let (($x652 (and $x536 $x273 (>= block_num_q0 block_num_2) (ite $x845 (ite $x836 $x972 (and $x986)) (ite $x836 $x972 (and $x714))))))
 (or (not $x652) $x519 $x738))))))))))))))))))))))))))))))))))))))))))))))))))))))))
 ))
 (let (($x511 (<= xa_q 2)))
 (let (($x512 (>= xa_q 0)))
 (let (($x513 (and $x512 $x511)))
 (and $x513 true $x674))))))
 ))
 (and $x671)))
(check-sat)
