.PHONY: compile run clean set-logic all

# Default value
DEFAULT_N_TRANSACTIONS := 100

# If no argument is provided, use the default value
ifndef N_Transactions
    N_Transactions := $(DEFAULT_N_TRANSACTIONS)
endif

compile: clean
	python3 main.py $(Contract) $(N_Transactions) $(N_Participants)
	python3 outputTrace.py
	python3 outputState.py
		
set-logic:
	@for Prop in $(wildcard out/*); do \
		for file in $$(find $$Prop/tracebased -type f -name '*.smt2' | sort); do \
			sed -i '1s/^/$(LOGIC)\n/' $$file; \
		done \
	done
	@for Prop in $(wildcard out/*); do \
		for file in $$(find $$Prop/statebased -type f -name '*.smt2' | sort); do \
			sed -i '1s/^/$(LOGIC)\n/' $$file; \
		done \
	done

run:
	@for Prop in $(wildcard out/*); do \
		echo "PROPERTY: $$Prop"; \
		foundUNSAT=false; \
		for file in $$(find $$Prop/statebased -type f -name '*.smt2' | sort); do \
			foundSAT=false; \
			output=$$($$SMT $$file); \
			if [ "$$output" = "unsat" ]; then \
				foundUNSAT=true; \
				break; \
			elif [ "$$output" = "sat" ]; then \
				foundSAT=true; \
			fi \
		done; \
		if [ "$$foundUNSAT" = "true" ]; then \
			echo "STRONG UNSAT (=> LIQUID)"; \
		elif [ "$$foundSAT" = "true" ]; then \
			echo "WEAK SAT (=> NOT LIQUID?)"; \
			for i in $$(find $$Prop/tracebased/ -mindepth 1 -maxdepth 1 -type d | sort); do \
				foundUNSAT=false; \
				for file in $$(find $$i -type f -name '*.smt2' | sort); do \
					foundSAT=false; \
					output=$$($$SMT $$file); \
					if [ "$$output" = "unsat" ]; then \
						foundUNSAT=true; \
						echo "WEAK UNSAT (=> LIQUID?)"; \
						break; \
					elif [ "$$output" = "sat" ]; then \
						foundSAT=true; \
					fi \
				done; \
				if [ "$$foundUNSAT" = "false" ] && [ "$$foundSAT" = "true" ] ; then \
					echo "STRONG SAT (=> NOT LIQUID)"; \
					break; \
				fi \
			done; \
		fi \
	done

clean:
	rm -rf out/*

all: compile run
