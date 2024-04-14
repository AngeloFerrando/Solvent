.PHONY: compile run clean set-logic all

# Default value
DEFAULT_N_TRANSACTIONS := 100
DEFAULT_N_PARTICIPANTS := 2
DEFAULT_SMT := z3
DEFAULT_Can_Transactions_Arrive_Any_time := true
Contract := './vault.sol'

# If no argument is provided, use the default value
ifndef N_Transactions
    N_Transactions := $(DEFAULT_N_TRANSACTIONS)
endif
ifndef N_Participants
    N_Participants := $(DEFAULT_N_PARTICIPANTS)
endif
ifndef Can_Transactions_Arrive_Any_time
    Can_Transactions_Arrive_Any_time := $(DEFAULT_Can_Transactions_Arrive_Any_time)
endif

compile: clean
	python3 ../../main.py $(Contract) $(N_Transactions) $(N_Participants) $(Can_Transactions_Arrive_Any_time)
	@if test -f ./out/outputTrace.py; then \
		python3 ./out/outputTrace.py; \
	fi
	@if test -f ./out/outputState.py; then \
		python3 ./out/outputState.py; \
	fi
		
set-logic:
	@for Prop in $(wildcard out/smt2/*); do \
		for file in $$(find $$Prop/tracebased -type f -name '*.smt2' | sort); do \
			sed -i '1s/.*/$(LOGIC)/' $$file; \
		done \
	done
	@for Prop in $(wildcard out/smt2/*); do \
		for file in $$(find $$Prop/statebased -type f -name '*.smt2' | sort); do \
			sed -i '1s/.*/$(LOGIC)/' $$file; \
		done \
	done

run:
	@if [ "$$SMT" = "cvc5" ]; then \
		smt_flag="--produce-models"; \
	else \
		smt_flag="";\
	fi; \
	for Prop in $(wildcard out/smt2/*); do \
		echo "PROPERTY: $$Prop"; \
		foundUNSAT=false; \
		for file in $$(find $$Prop/statebased -type f -name '*.smt2' | sort); do \
			foundSAT=false; \
			output=$$($$SMT $$file $$smt_flag); \
			# echo $$output; \
			if echo "$$output" | grep -q "error"; then \
				foundUNSAT=true; \
				break; \
			elif echo "$$output" | grep -q "sat"; then \
				foundSAT=true; \
			fi \
		done; \
		if [ "$$foundUNSAT" = "true" ]; then \
			echo "LIVE"; \
		else \
			# if [ "$$foundSAT" = "true" ]; then \
			# 	echo "WEAK SAT (=> NOT LIQUID?)"; \
			# fi; \
			for i in $$(find $$Prop/tracebased/ -mindepth 1 -maxdepth 1 -type d | sort); do \
				foundUNSAT=false; \
				for file in $$(find $$i -type f -name '*.smt2' | sort); do \
					foundSAT=false; \
					output=$$($$SMT $$file $$smt_flag); \
					# echo $$output; \
					if echo "$$output" | grep -q "error"; then \
						foundUNSAT=true; \
						ii=$$(echo $$i | rev | cut -d'/' -f1 | rev); \
						echo "LIVE UP TO $$ii TRANSACTION"; \
						break; \
					elif echo "$$output" | grep -q "sat"; then \
						foundSAT=true; \
					fi \
				done; \
				if [ "$$foundUNSAT" = "false" ] && [ "$$foundSAT" = "true" ]; then \
					echo "NOT LIVE (COUNTEREXAMPLE FOUND AND STORED IN $$Prop/counterexample.txt)"; \
					echo $$output > $$Prop/counterexample.txt; \
					break; \
				fi \
			done; \
			if [ "$$foundUNSAT" = "false" ] && [ "$$foundSAT" = "false" ]; then \
				echo "UNKNOWN"; \
			fi \
		fi \
	done

clean:
	rm -rf out/*
	rm -rf out

all: compile run
