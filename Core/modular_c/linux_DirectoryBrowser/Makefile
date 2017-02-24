DIR_INC = ./include
DIR_SRC = ./src
DIR_OBJ = ./obj
DIR_BIN = ./bin

SRC = $(wildcard ${DIR_SRC}/*.cpp)
OBJ = $(patsubst %.cpp,${DIR_OBJ}/%.o,$(notdir ${SRC}))

TARGET = main
BIN_TARGET = ${DIR_BIN}/${TARGET}

CC = g++
CFLAGS = -g -ggdb -Wall -I${DIR_INC}


$(BIN_TARGET):./main.cpp $(DIR_OBJ)/myDirBrowser.o
	$(CC) -o $@ -I$(CFLAGS) ./main.cpp $(DIR_OBJ)/myDirBrowser.o

$(DIR_OBJ)/myDirBrowser.o:$(DIR_SRC)/myDirBrowser.cpp
	$(CC) -o $(DIR_OBJ)/myDirBrowser.o -c -I$(CFLAGS) $(DIR_SRC)/myDirBrowser.cpp

#ALL:
#	@echo $(TARGET)
#	@echo $(BIN_TARGET)
#	@echo $(SRC)
#	@echo $(OBJ)
#	@echo $(CFLAGS)

