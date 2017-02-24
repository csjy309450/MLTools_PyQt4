#include "myDirBrowser.h"

using namespace std;

int main(int argc, char **argv)
{
    // 测试
    myDirBrowser test;
    if(argc>1)
       test.SetDirPath(std::string(argv[1]));

       test.CreateDirectory("/home/yangzheng/test");

//    test.GetAllFilesName();
//    //test.PrintAllFilesName();
//
//    std::string tmpStr;
//    while(test.GetNextFramePath(&tmpStr))
//        std::cout<<tmpStr<<std::endl;

    return 0;
}
