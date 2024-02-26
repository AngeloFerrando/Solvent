.PHONY: compile run clean all

compile: clean
	python3 main.py $(Contract) $(N_Transactions) $(N_Participants)
	python3 outputTrace.py
	python3 outputState.py

SUBDIRS := $(wildcard out/*)

run:
	@found=false; \
	sat=false; \
	for Prop in $(SUBDIRS); do \
		echo "PROPERTY: $$Prop"; \
		for file in $$(find $$Prop/tracebased -type f -name '*.smt2' | sort); do \
			output=$$($$SMT $$file); \
			if [ "$$output" = "sat" ]; then \
				found=true; \
				break; \
			fi \
		done; \
		if [ "$$found" = "true" ]; then \
			echo "STRONG SAT"; \
		else \
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
				echo "STRONG UNSAT"; \
			elif [ "$$sat" = "true" ]; then \
				echo "WEAK SAT"; \
			else \
				echo "UNKNOWN"; \
			fi \
		fi \
	done

clean:
	rm -rf out/*

all: compile run
