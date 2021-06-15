package com.example.sqliteexample;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.provider.BaseColumns;

public class PeopleDBHelper extends SQLiteOpenHelper {
    public static final String  DATABASE_NAME = "database";
    public static final int DATABASE_VERSION = 1;

    public PeopleDBHelper(Context context){
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase sqLiteDatabase){
        sqLiteDatabase.execSQL(PeopleContract.PeopleEntry.SQL_CREATE_TABLE);
    }

    @Override
    public void onUpgrade(SQLiteDatabase sqLiteDatabase, int oldVersion, int newVersion){
        // 단순히 데이터를 삭제하고 다시 시작하는 정책이 적용될 경우
        sqLiteDatabase.execSQL(PeopleContract.PeopleEntry.SQL_CREATE_TABLE);
        onCreate(sqLiteDatabase);
    }

    void insertRecord(String name, int age){
        SQLiteDatabase db = getReadableDatabase();

        ContentValues values = new ContentValues();
        values.put(PeopleContract.PeopleEntry.COLUMN_NAME, name);
        values.put(PeopleContract.PeopleEntry.COLUMN_AGE, age);

        db.insert(PeopleContract.PeopleEntry.TABLE_NAME, null, values);
    }

    public Cursor readRecordOrderByAge(){
        SQLiteDatabase db = getReadableDatabase();
        String[] projection = {
                BaseColumns._ID,
                PeopleContract.PeopleEntry.COLUMN_NAME,
                PeopleContract.PeopleEntry.COLUMN_AGE
        };

        String sortOrder = PeopleContract.PeopleEntry.COLUMN_AGE + " DESC";

        Cursor cursor = db.query(
                PeopleContract.PeopleEntry.TABLE_NAME,  // The table to query
                projection,         // The array of columns to return (pass null to get all)
                null,       // where 문에 필요한 column
                null,   // where 문에 필요한 value
                null,       // group by를 적용할 column
                null,       // having 절
                sortOrder           // 정렬 방식
        );

        return cursor;
    }
}
