#include <iostream>
#include <jdbc/mysql_driver.h>
#include <jdbc/mysql_connection.h>
#include <jdbc/cppconn/statement.h>
#include <jdbc/cppconn/resultset.h>
using namespace std;

int main() {
    try {
        sql::mysql::MySQL_Driver* driver = sql::mysql::get_mysql_driver_instance();
        unique_ptr<sql::Connection> conn(
            driver->connect("tcp://<rds_endpoint>:3306", "<id>", "<passwd>"));

        conn->setSchema("<db_name>");

        unique_ptr<sql::Statement> stmt(conn->createStatement());
        unique_ptr<sql::ResultSet> res(stmt->executeQuery("SELECT * FROM course"));

        while (res->next()) {
            cout << "course_id: " << res->getInt("course_id") << ", name: " << res->getString("name") << endl;
        }

    } catch (sql::SQLException& e) {
        cerr << "Error: " << e.what() << endl;
    }

    return 0;
}






