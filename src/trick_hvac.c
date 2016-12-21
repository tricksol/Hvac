/*
 ============================================================================
 Name        : trick_hvac.c
 Author      : Matthew Midgett /  Randy Gilliand
 Version     :
 Copyright   : Your copyright notice
 Description : C program to control HVAC using Raspberry Pi
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include </usr/include/mysql/my_global.h>
#include </usr/include/mysql/mysql.h>

int main(void) {

   MYSQL *conn;
   MYSQL_RES *res;
   MYSQL_ROW row;

   const char *server = "localhost";
   const char *user = "swriter";
   const char *password = "PASSWORD"; /* set me first */
   const char *database = "hvac";

   conn = mysql_init(NULL);

   /* Connect to database */
   if (!mysql_real_connect(conn, server,
         user, password, database, 0, NULL, 0)) {
      fprintf(stderr, "%s\n", mysql_error(conn));
      exit(1);
   }

   /* send SQL query */
   if (mysql_query(conn, "show tables")) {
      fprintf(stderr, "%s\n", mysql_error(conn));
      exit(1);
   }

   res = mysql_use_result(conn);

   /* output table name */
   printf("MySQL Tables in mysql database:\n");
   while ((row = mysql_fetch_row(res)) != NULL)
      printf("%s \n", row[0]);

   /* close connection */
   mysql_free_result(res);
   mysql_close(conn);
}
