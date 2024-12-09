.PHONY: compile run clean set-logic all

# Default value
DEFAULT_TIMEOUT := 300
DEFAULT_N_TRANSACTIONS := 100
DEFAULT_N_PARTICIPANTS := 2
DEFAULT_SMT := z3
DEFAULT_Can_Transactions_Arrive_Any_time := true
DEFAULT_Fixed_Iteration := -1
DEFAULT_State_Based := true
DEFAULT_Trace_Based := true
Contract := './auction.sol'

# If no argument is provided, use the default value
ifndef Timeout
    Timeout := $(DEFAULT_TIMEOUT)
endif
ifndef N_Transactions
    N_Transactions := $(DEFAULT_N_TRANSACTIONS)
endif
ifndef N_Participants
    N_Participants := $(DEFAULT_N_PARTICIPANTS)
endif
ifndef Can_Transactions_Arrive_Any_time
    Can_Transactions_Arrive_Any_time := $(DEFAULT_Can_Transactions_Arrive_Any_time)
endif
ifndef Fixed_Iteration
    Fixed_Iteration := $(DEFAULT_Fixed_Iteration)
endif
ifndef State_Based
    State_Based := $(DEFAULT_State_Based)
endif
ifndef Trace_Based
    Trace_Based := $(DEFAULT_Trace_Based)
endif

compile: 
	python3 ../../../src/main.py $(Contract) $(N_Transactions) $(N_Participants) $(Can_Transactions_Arrive_Any_time) $(Fixed_Iteration)
	@if $(Trace_Based); then \
		if test -f ./out/outputTrace.py; then \
			python3 ./out/outputTrace.py; \
		fi \
	fi
	@if $(State_Based); then \
		if test -f ./out/outputState.py; then \
			python3 ./out/outputState.py; \
		fi \
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
		if $(State_Based); then \
			for file in $$(find $$Prop/statebased -type f -name '*.smt2' | sort); do \
				foundSAT=false; \
				output=$$(time ; timeout $(Timeout) $$SMT $$file $$smt_flag); \
				echo $$output; \
				if echo "$$output" | grep -q "error"; then \
					foundUNSAT=true; \
					break; \
				elif echo "$$output" | grep -q "sat"; then \
					foundSAT=true; \
				fi \
			done; \
		fi; \
		if [ "$$foundUNSAT" = "true" ]; then \
			echo "LIQUID"; \
		else \
			# if [ "$$foundSAT" = "true" ]; then \
			# 	echo "WEAK SAT (=> NOT LIQUID?)"; \
			# fi; \
			if $(Trace_Based); then \
				for i in $$(find $$Prop/tracebased/ -mindepth 1 -maxdepth 1 -type d | sort); do \
					foundUNSAT=false; \
					for file in $$(find $$i -type f -name '*.smt2' | sort); do \
						foundSAT=false; \
						output=$$(date ; timeout $(Timeout) $$SMT $$file $$smt_flag); \
						echo $$output; \
						if echo "$$output" | grep -q "error"; then \
							foundUNSAT=true; \
							ii=$$(echo $$i | rev | cut -d'/' -f1 | rev); \
							echo "LIQUID UP TO $$ii TRANSACTION"; \
							break; \
						elif echo "$$output" | grep -q "sat"; then \
							foundSAT=true; \
						fi; \
					done; \
					if [ "$$foundUNSAT" = "false" ] && [ "$$foundSAT" = "true" ]; then \
						echo "NOT LIQUID (COUNTEREXAMPLE FOUND AND STORED IN ./$$Prop.counterexample)"; \
						echo $$output > ./$$Prop.raw; \
						ii=$$(echo $$i | rev | cut -d'/' -f1 | rev); \
						python3 ../../../src/parseTrace.py ./$$Prop.raw $$ii > ./$$Prop.counterexample; \
						break; \
					fi; \
				done; \
				if [ "$$foundUNSAT" = "false" ] && [ "$$foundSAT" = "false" ]; then \
					echo "UNKNOWN"; \
				fi; \
			fi; \
		fi; \
	done;

clean:
	rm -rf out/*
	rm -rf out

all: compile run
