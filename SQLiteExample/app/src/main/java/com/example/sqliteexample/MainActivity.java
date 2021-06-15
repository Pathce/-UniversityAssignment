package com.example.sqliteexample;

import androidx.appcompat.app.AppCompatActivity;

import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.os.Bundle;
import android.provider.BaseColumns;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    private PeopleDBHelper dbHelper;
    private TextView textView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        textView = (TextView) findViewById(R.id.textView);

        dbHelper = new PeopleDBHelper(this);
        dbHelper.insertRecord("갑", 33);
        dbHelper.insertRecord("을", 21);
        dbHelper.insertRecord("병", 44);
        dbHelper.insertRecord("정", 17);

        printTable();
    }

    private void printTable(){
        Cursor cursor = dbHelper.readRecordOrderByAge();
        String result = "";

        result += "row count : " + cursor.getCount() + "\n";
        while (cursor.moveToNext()){
            int itemId = cursor.getInt(cursor.getColumnIndexOrThrow(PeopleContract.PeopleEntry._ID));
            String name = cursor.getString(cursor.getColumnIndexOrThrow(PeopleContract.PeopleEntry.COLUMN_NAME));
            int age = cursor.getInt(cursor.getColumnIndexOrThrow(PeopleContract.PeopleEntry.COLUMN_AGE));

            result += itemId + " " + name + " " + age + "\n";
        }

        textView.setText(result);
        cursor.close();
    }

    @Override
    protected void onDestroy(){
        dbHelper.close();
        super.onDestroy();
    }
}