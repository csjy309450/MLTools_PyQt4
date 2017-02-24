#include "myDirBrowser.h"

myDirBrowser::myDirBrowser()
{
    //ctor
    m_dirPath = "/home/yangzheng/testData/ucsd/vidf1_33_000.y";
    m_currentFrame = 0;
}

myDirBrowser::~myDirBrowser()
{
    //dtor
}

void myDirBrowser::SetDirPath(std::string dirPath)
{
    if(!dirPath.empty())
        m_dirPath = dirPath;
}

/* Get all files under dir_name , do not show directories ! */
void myDirBrowser::GetAllFilesName()
{
    // check the parameter !
    if(m_dirPath.empty())
    {
        cout<<" directory name is null ! "<<endl;
        return;
    }

    // check if m_dirPath is a valid dir
    struct stat s;
    lstat( m_dirPath.c_str() , &s );
    if( ! S_ISDIR( s.st_mode ) )
    {
        cout<<"directory name is not a valid directory !"<<endl;
        return;
    }

    struct dirent * filename;    // return value for readdir()
    DIR * dir;                   // return value for opendir()
    dir = opendir( m_dirPath.c_str() );
    if( NULL == dir )
    {
        cout<<"Can not open dir "<<m_dirPath.c_str()<<endl;
        return;
    }
    cout<<"Successfully opened the dir !"<<endl;

    /* read all the files in the dir ~ */
    while( ( filename = readdir(dir) ) != NULL )
    {
        // get rid of "." and ".."
        if( strcmp( filename->d_name , "." ) == 0 ||
            strcmp( filename->d_name , "..") == 0    )
            continue;
        m_files.push_back(std::string(filename->d_name));
    }
    ::sort(m_files.begin(), m_files.end());
}

void myDirBrowser::PrintAllFilesName()
{
    if(m_files.empty())
    {
        std::cout<<"Directory have no files"<<std::endl;
        return;
    }
    for(std::vector<std::string>::iterator iter = m_files.begin();iter!=m_files.end();iter++)
    {
        std::cout<<*iter<<std::endl;
    }
}

std::string myDirBrowser::GetNextFramePath()
{
    if(IsLastFrame())
        return "At the end of sequence!";
    return m_dirPath+"/"+m_files[m_currentFrame++];
}

int myDirBrowser::CreateDirectory(std::string dirPath)
{
    return mkdir(dirPath.c_str(), S_IRWXU | S_IRWXG | S_IROTH | S_IXOTH);
}

bool myDirBrowser::GetNextFramePath(std::string *outFilePath)
{
    if(IsLastFrame())
        return false;
    *outFilePath = m_dirPath+"/"+m_files[m_currentFrame++];
    return true;
}
