#include <stdio.h>
#include <dirent.h>
#include <string>

using namespace std;
int main(void)
{
    DIR * rep = opendir(".");
    
    if (rep != NULL)
    {
        struct dirent * ent;
        
        while ((ent = readdir(rep)) != NULL)
        {
            string str(ent->d_name);
            string s = "." + ent->d_name;
            DIR * rep2 = opendir(s);
            struct dirent * ent2;
            
            while ((ent = readdir(rep)) != NULL)
            {
                printf("%s\n", ent2->d_name);
            }
            printf("%s\n", ent->d_name);
        }
        
        closedir(rep);
    }
    
    return 0;
}
