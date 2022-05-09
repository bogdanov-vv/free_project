run:
	docker run -it test:2.3

list:
	docker image ls

prune_cont:
	docker container prune

prune_image:
	docker image prune
