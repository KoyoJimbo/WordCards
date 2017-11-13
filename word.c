#include<stdio.h>
#include<string.h>
#include<time.h>
#include<stdlib.h>


#define WORD_NUM 8
#define UNIT_NUM 2


typedef struct Unit {
    char ScrAns[WORD_NUM][30];
    char sQes[WORD_NUM][200];
}Unit;


int fRnd(void);

void initUnit(Unit *unit);

int Unitele(void);

void sJudge(Unit *unit,int rnd,int unitNo);

int ftimes(void);


int main(void)
{
    Unit unit[UNIT_NUM];

    int rnd;
    int up_to;
    int times;
    int unitNo;


//  構造体の初期設定を行っています。
    initUnit(unit);


    unitNo = Unitele();


    printf("\n");


    up_to  = ftimes();


    printf("\n");


    for(times=0;times<up_to;times++){

        printf("%d回目",times+1);


//      乱数の処理を行っています。
        rnd = fRnd();


//      入力と正誤判定を行ないます。
        sJudge(unit,rnd,unitNo);

    }
    

    return 0;
}


int Unitele(void)
{
    int tmp;
    int unitNo = 0;
    printf("Unit番号を指定してください。(6 or 8):");
    scanf("%d",&tmp);
    if(tmp == 8){
        unitNo = 1;
    }

    return unitNo;
}


int ftimes(void){
    int i;
    printf("連続回答数を指定してください。:");
    scanf("%d",&i);
    return i;
}


void sJudge(Unit *unit,int rnd,int unitNo){
    char str[30];

    printf("No.%d\n",rnd);

    printf("\n");

    printf("%s\n",*(unit[unitNo].sQes+rnd));

    printf("\n");

    printf("文字列を入力してください。\n");
    scanf("%s",str);

    printf("\n");

    if(strcmp(str,*(unit[unitNo].ScrAns+rnd)) == 0){

        printf("正解です。\n");

    }else{

        printf("違います\n");
        printf("%s\n",*(unit[unitNo].ScrAns+rnd));

    }
    printf("\n");
}


int fRnd(void)
{
    int rnd;

	srand((unsigned int)time(NULL));
	rnd = rand()%(WORD_NUM-1);

    return rnd;
}


void initUnit(Unit *unit)
{

    strcpy(unit[0].ScrAns[0],"generation");
    strcpy(unit[0].ScrAns[1],"material");
    strcpy(unit[0].ScrAns[2],"inspriration");
    strcpy(unit[0].ScrAns[3],"mundane");
    strcpy(unit[0].ScrAns[4],"risk");
    strcpy(unit[0].ScrAns[5],"audition");
    strcpy(unit[0].ScrAns[6],"pass on");
    strcpy(unit[0].ScrAns[7],"previous");

    strcpy(unit[1].ScrAns[0],"giraffe");
    strcpy(unit[1].ScrAns[1],"president");
    strcpy(unit[1].ScrAns[2],"racism");
    strcpy(unit[1].ScrAns[3],"apatheid");
    strcpy(unit[1].ScrAns[4],"right");
    strcpy(unit[1].ScrAns[5],"plateau");
    strcpy(unit[1].ScrAns[6],"silhouette");
    strcpy(unit[1].ScrAns[7],"fabulous");

    strcpy(unit[0].sQes[0],"the people born and living about the same time, considered as a group");
    strcpy(unit[0].sQes[1],"documents that are used for a particular activity");
    strcpy(unit[0].sQes[2],"to tell somenoe something that someone else  has told you");
    strcpy(unit[0].sQes[3],"very ordinary and therfore not interesting");
    strcpy(unit[0].sQes[4],"the possibility of something bad happening");
    strcpy(unit[0].sQes[5],"a short performance that someone givis to try to get a job as an actor,etc");
    strcpy(unit[0].sQes[6],"someone or something that gives you ideas for doing something");
    strcpy(unit[0].sQes[7],"existing or happening before this one");

    strcpy(unit[1].sQes[0],"a tall african animal with a very long neck and legs");
    strcpy(unit[1].sQes[1],"the leader of government in some countries");
    strcpy(unit[1].sQes[2],"the bilief that some races of people are better than others");
    strcpy(unit[1].sQes[3],"a thing that you ar");
    strcpy(unit[1].sQes[4],"the former social system in south afica of separating people of different people of different races");
    strcpy(unit[1].sQes[5],"a dark shape seen against a light background");
    strcpy(unit[1].sQes[6],"jlf");
    strcpy(unit[1].sQes[7],"very good");

}
