AIRSIM_CONTAINER_NAME=airsim
NVIDIA_CONTAINER_NAME=airsim:1.8.1

UNREAL_BINARY_PATH=/home/ajay/work/Airsim/AirSim/docker/Blocks/LinuxNoEditor/Blocks.sh
SDL_VIDEODRIVER_VALUE=

up:
	xhost +local:docker
	docker compose up -d

enter:
	xhost +local:docker
	docker exec -it ${AIRSIM_CONTAINER_NAME} bash -c "./docker/Blocks/LinuxNoEditor/Blocks.sh -opengl4 -windowed -ResX=854 -ResY=480"


down:
	docker compose down



