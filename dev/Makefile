build:
	docker build -t git01.iis.fhg.de:5005/mkj/vscode-extension-of-the-week .

run: build
	docker run -d -it --rm git01.iis.fhg.de:5005/mkj/vscode-extension-of-the-week

push: build
	docker login git01.iis.fhg.de:5005
	docker push git01.iis.fhg.de:5005/mkj/vscode-extension-of-the-week
