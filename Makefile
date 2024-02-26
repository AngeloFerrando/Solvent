.PHONY: compile run clean all

compile: clean
	python3 main.py $(Contract) $(N_Transactions) $(N_Participants)
	python3 outputTrace.py
	@for Prop in $(wildcard out/*); do \
		for file in $$(find $$Prop/tracebased -type f -name '*.smt2' | sort); do \
			sed -i '1s/^/$(LOGIC)\n/' $$file; \
		done \
	done
	python3 outputState.py
	@for Prop in $(wildcard out/*); do \
		for file in $$(find $$Prop/statebased -type f -name '*.smt2' | sort); do				           	sed -i '1s/^/$(LOGIC)\n/' $$file; \
		done \
	done	

run:
	@for Prop in $(wildcard out/*); do \
		echo "PROPERTY: $$Prop"; \
		sat=false; \
		for i in $$(find $$Prop/tracebased/ -mindepth 1 -maxdepth 1 -type d | sort); do \
			foundSAT=false; \
			foundUNSAT=false; \
			for file in $$(find $$i -type f -name '*.smt2' | sort); do \
				output=$$($$SMT $$file); \
				if [ "$$output" = "unsat" ]; then \
					foundUNSAT=true; \
					break; \
				elif [ "$$output" = "sat" ]; then \
					foundSAT=true; \
				fi \
			done; \
			if [ "$$foundUNSAT" = "false" ] && [ "$$foundSAT" = "true" ] ; then \
				echo "STRONG SAT (=> NOT LIQUID)"; \
				sat=true; \
				break; \
			fi \
		done; \
		if [ "$$sat" = "false" ]; then \
			foundUNSAT=false; \
			foundSAT=false; \
			for file in $$(find $$Prop/statebased -type f -name '*.smt2' | sort); do \
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
			else \
				echo "UNKNOWN (=> ??)"; \
			fi \
		fi \
	done

clean:
	rm -rf out/*

all: compile run
