package com.example.secondapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    private int count = 0;
    private TextView label;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        Button inc;
        Button reset;
        Button dec;

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        label = findViewById(R.id.textView);

        inc = findViewById(R.id.button);
        dec = findViewById(R.id.button2);
        reset = findViewById(R.id.button3);

        inc.setOnClickListener(v -> {
            showToast("Increment");
            increment();
        });

        dec.setOnClickListener(v -> {
            showToast("Decrement");
            decrement();
        });

        reset.setOnClickListener(v -> {
            showToast("Reset");
            setReset();
        });
    }

    private void increment() {
        count++;
        label.setText(String.valueOf(count));
    }

    private void decrement() {
        count--;
        label.setText(String.valueOf(count));
    }
    private void setReset() {
        count = 0;
        label.setText(String.valueOf(count));
    }

    private void showToast(String message) {
        Toast.makeText(this, message, Toast.LENGTH_SHORT).show();
    }
}