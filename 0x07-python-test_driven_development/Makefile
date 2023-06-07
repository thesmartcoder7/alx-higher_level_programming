run:
	chmod +x *.py && pycodestyle *.py

betty:
	betty *.c

tests:
	./test.py

clear cache:
	git rm -r --cached . && git add . && git commit -m "chore: clear git cache" && git push
	