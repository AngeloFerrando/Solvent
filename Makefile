.PHONY: compile run clean all

compile: clean
	python3 main.py $(Contract) $(N_Transactions) $(N_Participants)
	python3 outputTrace.py
	python3 outputState.py

SUBDIRS := $(wildcard out/*)

run:
	@for Prop in $(SUBDIRS); do \
		echo "PROPERTY: $$Prop"; \
		sat=false; \
		for i in $$(find $$Prop/tracebased/ -mindepth 1 -maxdepth 1 -type d | sort); do \
			found=false; \
			for file in $$(find $$i -type f -name '*.smt2' | sort); do \
				output=$$($$SMT $$file); \
				if [ "$$output" = "unsat" ]; then \
					found=true; \
					break; \
				fi \
			done; \
			if [ "$$found" = "false" ]; then \
				echo "STRONG SAT (=> NOT LIQUID)"; \
				sat=true; \
				break; \
			fi \
		done; \
		if [ "$$sat" = "false" ]; then \
			found=false; \
			for file in $$(find $$Prop/statebased -type f -name '*.smt2' | sort); do \
				output=$$($$SMT $$file); \
				if [ "$$output" = "unsat" ]; then \
					found=true; \
					break; \
        		elif [ "$$output" = "sat" ]; then \
					sat=true; \
				fi \
			done; \
    	    if [ "$$found" = "true" ]; then \
				echo "STRONG UNSAT (=> LIQUID)"; \
			elif [ "$$sat" = "true" ]; then \
				echo "WEAK SAT (=> NOT LIQUID?)"; \
			else \
				echo "UNKNOWN (=> ??)"; \
			fi \
		fi \
	done

clean:
	rm -rf out/*

all: compile run
