#include "httplib.h"
#include "json.hpp"
#include <iostream>
using namespace std;
using namespace httplib;
using namespace nlohmann;


// 0. 메인
//      1. 로그인/회원가입
//          1.1 로그인
//          1.2 회원 가입
//      2. 사용자
//          2.1 비밀번호 바꾸기
//      3. 소셜
//          3.1 포스팅 생성
//          3.2 포스팅 전체 스레드 보기
//          3.3 포스팅 삭제 

Client cli("http://43.201.118.45:5001");  // EC2 퍼블릭 IP

//Global 변수
//1.로그인 한 user_id (보통 id는 0부터 시작할 때가 많아서 -1로 하는게 좋을 듯)
int user_id = 0; 

json send_request(string method, string endpoint, json body = {}) {
    Result res;

    if (method == "GET")
        res = cli.Get(endpoint.c_str());
    else if (method == "POST")
        res = cli.Post(endpoint.c_str(), body.dump(), "application/json");
    else if (method == "PATCH")
        res = cli.Patch(endpoint.c_str(), body.dump(), "application/json");
    else if (method == "DELETE")
        res = cli.Delete(endpoint.c_str(), body.dump(), "application/json");

    if (res) {
        return json::parse(res->body);
    } else {
        return json{
            {"status", "request failed"},
            {"reason", "no response received"}
        };
    }
}

void m_3_4_createcomment() {
    string post_id, text;

    cout << "[댓글 작성]" << endl;
    cout << "댓글을 작성할 포스트 ID를 입력하세요: ";
    cin >> post_id;
    cin.ignore(); // 개행 문자 제거

    cout << "댓글 내용을 입력하세요: ";
    getline(cin, text);

    json body;
    body["post_id"] = post_id;
    body["text"] = text;

    string endpoint = "/comment/" + to_string(user_id);
    json response = send_request("POST", endpoint, body);

    cout << "status: " << response["status"] << endl;
    if (response.contains("reason"))
        cout << "reason: " << response["reason"] << endl;

    cout << endl;
}


void m_3_5_getcomment() {
    string post_id;

    cout << "포스트 코멘트 조회" << endl;
    cout << "포스트 아이디:" << endl;
    cin >> post_id; 
    
    string endpoint = "/comment/check?post_id=" + post_id;
    json response = send_request("GET", endpoint);

    cout << "status: " << response["status"] << endl;

    if (response.contains("result") && response["result"].is_array()) {
        for (auto& comment : response["result"]) {
            cout << "post_id: " << comment["user_id"] << endl;
            cout << "text   : " << comment["text"] << endl;
            cout << "--------------------" << endl;
        }
    } else if (response.contains("reason")) {
        cout << "reason: " << response["reason"] << endl;
    }

    cout << endl;
}

void m_3_3_postdelete(){
    string post_id;

    cout << "포스팅 삭제" << endl;
    cout << "포스트 아이디:" << endl;
    cin.ignore();              
    getline(cin, post_id);      

    json body;
    body["post_id"] = post_id;

    string endpoint = "/posting/delete";

    json response = send_request("DELETE", endpoint, body);

    cout << "status: " << response["status"] << endl;

    if (response.contains("reason"))
        cout << "reason: " << response["reason"] << endl;

}

void m_3_2_allpost() {
    cout << "작성한 포스팅 스레드" << endl;

    string endpoint = "/posting/check";

    json response = send_request("GET", endpoint);

    cout << "status: " << response["status"] << endl;

    if (response.contains("result") && response["result"].is_array()) {
        for (auto& post : response["result"]) {
            cout << "post_id: " << post["post_id"] << endl;
            cout << "title: " << post["title"] << endl;
            cout << "text: " << post["text"] << endl;
            cout << "--------------------" << endl;
        }
    } else {
        cout << "포스팅이 없습니다" << endl;
    }

    if (response.contains("reason"))
        cout << "reason: " << response["reason"] << endl;

}


void m_3_1_posting() {
    string title, post_text;

    cout << "포스팅 생성" << endl;
    cout << "포스트 제목:" << endl;
    cin.ignore(); // 버퍼에 남은 개행 제거
    getline(cin, title);

    cout << "포스트 내용:" << endl;
    getline(cin, post_text);

    json body;
    body["title"] = title;
    body["post_text"] = post_text;

    string endpoint = "/posting/" + to_string(user_id) + "/create";

    json response = send_request("POST", endpoint, body);

    cout << "status: " << response["status"] << endl;

    if (response.contains("post_id"))
        cout << "post_id: " << response["post_id"] << endl;

    if (response.contains("reason"))
        cout << "reason: " << response["reason"] << endl;

}



void m_3_social() {
    while (1) {
        int i;
        cout << "[소셜 기능]" << endl;
        cout << "1. 포스팅 생성" << endl;
        cout << "2. 포스팅 전체 스레드 보기" << endl;
        cout << "3. 포스팅 삭제" << endl;
        cout << "4. 댓글 작성" << endl;
        cout << "5. 내가 작성한 댓글 조회" << endl;
        cout << "6. 돌아가기" << endl;
        cout << "번호를 입력하세요: ";
        cin >> i;
        cin.ignore(numeric_limits<streamsize>::max(), '\n'); 

        switch (i) {
            case 1:
                m_3_1_posting();
                break;
            case 2:
                m_3_2_allpost();
                break;
            case 3:
                m_3_3_postdelete();
                break;
            case 4:
                m_3_4_createcomment();
                break;
            case 5:
                m_3_5_getcomment();
                break;
            case 6:
                return;
            default:
                break;
        }
    }
}


void m_2_user_pwchange() {
    string pw, new_pw;
    cin.ignore();

    cout << "비밀번호 변경" << endl;
    cout << "기존 비밀번호" << endl;
    getline(cin, pw);
    cout << "새 비밀번호" << endl;
    getline(cin, new_pw);

    json body;
    body["pw"] = pw;
    body["newPW"] = new_pw;

    string endpoint = "/user/" + to_string(user_id) + "/password_change";

    json response = send_request("PATCH", endpoint, body);

    cout << "status: " << response["status"] << endl;

    if (response.contains("reason"))
        cout << "reason: " << response["reason"] << endl;
}


void m_2_user(){
    while(1){
        int i;
        cout << "[사용자 기능]" << endl;
        cout << "1. 비밀번호 바꾸기" << endl;
        cout << "3. 돌아가기" << endl;

        cin >> i;

        switch(i){
            case 1:
                m_2_user_pwchange();
                break;
            case 3:
                return;
            default:
                break;
        }

    }

}

void m_1_2_signup() {
    string nickname, pw, name, age, email;

    cout << "[회원가입]" << endl;

    cout << "nickname (필수)" << endl;
    cin >> nickname;

    cout << "pw(필수)" << endl;
    cin >> pw;

    cout << "name(필수)" << endl;
    cin >> name;

    cin.ignore(); // cin 후 getline을 위한 buffer clear

    cout << "age(선택), 없으면 enter" << endl;
    getline(cin, age);

    cout << "email(선택), 없으면 enter" << endl;
    getline(cin, email);

    json body;
    body["nickname"] = nickname;
    body["pw"] = pw;
    body["name"] = name;

    if (!age.empty()) {
        body["age"] = age;
    }
    if (!email.empty()) {
        body["email"] = email;
    }

    json response = send_request("POST", "/user/create", body);

    cout << "status: " << response["status"] << endl;

    if (response.contains("new user id")) {
        cout << "new_user_id: " << response["new user id"] << endl;
        user_id = response["new user id"];
    }

    if (response.contains("reason")) {
        cout << "reason: " << response["reason"] << endl;
    }

}


void m_1_1_login() {
    string nickname, pw;

    cout << "[로그인]" << endl;
    
    cout << "nickname (필수)" << endl;
    cin >> nickname;

    cout << "pw(필수)" << endl;
    cin >> pw;

    json body;
    body["nickname"] = nickname;
    body["pw"] = pw;

    json response = send_request("POST", "/user/login", body);

    cout << "status: " << response["status"] << endl;

    if (response.contains("login user")) {
        cout << "login user: " << response["login user"] << endl;
        user_id = response["login user"];
    }

    if (response.contains("reason")) {
        cout << "reason: " << response["reason"] << endl;
    }
}


void m_1_loginandsignup() {
    while (user_id == 0) {
        // 메뉴 출력
        cout << "[1. 로그인 및 회원 가입]" << endl;
        cout << "1. 로그인" << endl;
        cout << "2. 회원가입" << endl;
        cout << "3. 돌아가기" << endl;
 
        // 사용자 입력 처리
        int input;
        cin >> input;

        switch(input) {
            case 1:
                m_1_1_login();
                break;
            case 2:
                m_1_2_signup();
            case 3:
                return;
            default:
                break;
        }
    }
}

void m_0_mainMenu() {

    while (1) {
        // 메뉴 출력
        cout << "[홈메뉴]" << endl;
        cout << "1. 로그인 및 회원 가입" << endl;
        cout << "2. 사용자" << endl;
        cout << "3. 소셜" << endl;

        // 사용자 입력 처리
        int input;
        cin >> input;
        switch(input) {
            case 1:
                m_1_loginandsignup();
                break;
            case 2: //user_id 확인하는 절차를 m_2_user 안에 앞쪽에다가 기술하는 거 추천 (while 전에)
                if (user_id > 0) {
                    m_2_user(); 
                } else {
                    cout << "[알림] 로그인 후 이용 가능한 메뉴입니다." << endl;
                }
                break;
            case 3://user_id 확인하는 절차를 m_3_social 안에 앞쪽에다가 기술하는 거 추천 (while 전에)
                if(user_id > 0) {
                    m_3_social();
                }else{
                    cout << "[알림] 로그인 후 이용 가능한 메뉴입니다." << endl;
                }
            default:
                break;
        }
    }
}


int main() {
    m_0_mainMenu();
    
    return 0;

}
