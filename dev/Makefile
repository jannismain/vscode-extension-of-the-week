build:
	docker build -t git01.iis.fhg.de:5005/mkj/vscode-extension-of-the-week .

buildx:
	docker buildx build --platform linux/amd64 --push -t git01.iis.fhg.de:5005/mkj/vscode-extension-of-the-week .

run: build
	docker run -d -it --rm --entrypoint /bin/bash git01.iis.fhg.de:5005/mkj/vscode-extension-of-the-week

push: build
	docker login git01.iis.fhg.de:5005
	docker push git01.iis.fhg.de:5005/mkj/vscode-extension-of-the-week
