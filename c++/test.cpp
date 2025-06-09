#include <iostream>
using namespace std;

 struct fishBreadInfo{
        string flavor= "";
        float price = 0;
        int num = 0;
    };

class Fishbread{
public:
    fishBreadInfo info;

    Fishbread(){
        cout << "붕어빵 만들기 시작!" << endl;
    }

    void setInfo(){
        cout << "어떤 속을 넣을까요?" << endl;
        cin >> info.flavor ;
        cout << "한 개 가격은?" << endl;
        cin >> info.price;
        cout << "몇 개 만들기?" << endl;
        cin >> info.num ;

    }

    void showInfo(){
        cout << "붕어빵 정보" << endl;
        cout << "속재료: " << info.flavor << endl;
        cout << "갯수: " << info.price << endl;
        cout << "총 가격: " << info.price * info.num << endl;

    }

    ~Fishbread(){
        cout << "붕어빵 만들기 끝!" << endl;
    }
};

int main() {
    Fishbread a;
    a.setInfo();
    a.showInfo();
    return 0;
}

//구조체 Student
// struct Student{
//     string name;
//     float scores[3];
//     float avg;
// };
    // Student students[3];

    // for(int i=0; i <3; i++){
    //     cin >> students[i].name;
    //     for(int j =0; j<3;j++){
    //         cin >> students[i].scores[j];
    //     }
    // }
    // // 최고 점수를 받은 학생 찾기 

    // float maxScore = 0;
    // Student maxStudent;

    // for(int i =0; i<3; i++){
    //     //평균 점수 구하기
    //     float avg = (students[i].scores[0] + students[i].scores[1] + students[i].scores[2])/3;
        
    //     // 평균 점수 학생 구조체에 저장
    //     students[i].avg = avg;

    //     //최고 점수 판단 & 기록
    //     if(maxScore < avg) {
    //         maxScore = avg;
    //         maxStudent = students[i];
    //     }

    //     //최고 점수 학생 이름, 평균 점수 출력
    //     cout << maxStudent.name << endl;
    //     cout << maxStudent.avg << endl;
    // }



    // return 0;
    


// 별 찍기
    // int input = 0;
    // std:: cout << "피라미드의 높이를 입력하시오: " << std::endl;
    // std:: cin >> input; 

    // std::cout << "output: "<< std:: endl;

    // for(int i = 1; i <= input; i++){
    //     for(int k = 1; k <= input - i ; k++){
    //         std::cout <<" ";
    //     }

    //     for(int k = 1; k<= i * 2 - 1; k++){
    //         std::cout << "*";
    //     }
    //     std::cout<<std::endl;


//    int n = 1;
//    int sum = 0;

//    do {
//     std::cout << "숫자를 입력하세요 (0:exit) : " << std::endl;
//     std::cin >>n;
//     sum += n;
//    }
//    while (n != 0);
//    std:: cout << "사용자가 입력한 숫자의 합: " << sum <<std:: endl;

//  int i = 2;
//     int k = 1;
//     //2단  출력 
//     while(k<=9){
//         std::cout <<"2단 하나만 출력" <<"----------" << std::endl;
//         std::cout << i << "*" << k << i * k << std::endl;
//         k++; 
//     }


//     // 전체 구구단 출력;
//     while (i <= 9){
//         std::cout << i << "단 출력 "<<"____" << std::endl;

//         for(int k = 1; k<=9; k++){
//             std::cout << i << "*" << k << "=" << i * k << std:: endl;
//         }
//         i++;
//     }
    
//     //1부터 n까지 합 구하기 while문 버전
//     int n;
//     int sum = 0;
//     int j = 1;
//     std::cin >> n;

//     while (j <= n) {
//         sum += j;
//         ++j;
//     }
//     std:: cout << n << "까지의 합 " << sum << std::endl;

//    int val;
//    int result = 0;
//    std::cout << "1부터 n까지의 합 구하기"<< std::endl;
//    std::cout << "숫자(양의 정수)를 입력하세요 :" << std::endl;

//    std::cin >> val;
   
//    for(int i = 0; i <= val; i++){
//     result += i;
//    }

//    std::cout << "1부터 100까지의 합은 : " <<result << std::endl;


//test
//   std::string x;
//     std:: cout << "단어를 입력하세요" << std::endl;
//     std::cin >> x;
//     std::cout << "hello world - " << x << std::endl;


//  //5단 출력
//     std::cout << "5단출력" << std::endl;
//     int val = 5;
//     char times = '*';
//     char equal = '=';
//     for(int i = 1; i <= 10; i ++){
//         std::cout << val << times << i << equal << val * i << std::endl;
//     }
//     //1~9단 출력
//     for(int i = 1; i<= 9; i++){
//         std::cout<<"-----"<< i << "단 출력" <<"----"<< std::endl;
//         for(int k = 1; k<=9; k++){
//             std::cout << i << times << k << equal << i * k << std:: endl;
//         }
//     }