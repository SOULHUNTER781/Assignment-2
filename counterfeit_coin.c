#include<stdio.h>
int c,d,k,count=0;
int div(int l,int h);
int comp(int,int);
int main(int argc, char *argv[])
{
    int a,s=1;
    k=atoi(argv[s++]);
    c=atoi(argv[s++]);
    d=atoi(argv[s++]);
    a=div(1,k);
    if(a==-1)
        printf("There is no Counterfeit coin\n");
    else
    {
        printf("The Counterfeit coin is %d\n",a);
    }
        printf("The Number of Count taken is %d\n",count);
}
int div(int l,int h)
{
    int m;
    m=(l+h)/2;
    if(comp(l,h)==+1)
    {
        if(l==h)

            return h;

        if(d==1)
        {
            count++;
           return div(l,m);

        }
        else
        {
            count++;
            return div(m+1,h);

        }
    }
     else if(comp(l,h)==-1)
    {
        if(l==h)

            return h;

        if(d==1)
        {
            count++;
           return div(m+1,h);

        }
        else

        {
            count++;
            return div(l,m);

        }
    }
    else if(comp(l,h)==0)
    {
        count++;
        return -1;
    }
}
int comp(int l,int h)
{
    int m;
    m=(l+h)/2;
    if(c>=l&&c<=m)
        return(-1+2*d);
  else if(c<=h&&c>m)
        return(1-2*d);
  else
        return 0;

}
