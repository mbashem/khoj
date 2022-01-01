package com.example.myapplication

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.LinearLayout
import androidx.appcompat.app.AppCompatActivity
import androidx.constraintlayout.widget.ConstraintLayout
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class ClusterSearchActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        supportActionBar?.hide()
        setContentView(R.layout.cluster_search)

        var searchClicked = false

        val layoutview = findViewById<View>(R.id.thisview) as LinearLayout
        val SearchButton  = findViewById<Button>(R.id.ClusterSearchButton) as Button



        SearchButton.setOnClickListener(){

            var searchtext = findViewById<EditText>(R.id.editTextInput) as EditText

            if(searchtext.text.toString() != ""){

                //do api call here then populate SearcResultList with SearchResult objects

                val SearchResultList = mutableListOf<SearchResult>()
                //SearchResultList.add(SearchResult("A url","A text"))
                //SearchResultList.add(SearchResult("A url 2","A text 2"))

                if(!searchClicked) {
                    LayoutInflater.from(this).inflate(R.layout.recyclerview,layoutview,true)
                    val rv = findViewById<View>(R.id.recyclerviewlayoutRV) as RecyclerView
                    rv.layoutManager = LinearLayoutManager(this)
                    rv.adapter = rv_ClusterSearchAdapter(SearchResultList)
                    searchClicked = true
                }
                else {

                    var rv = findViewById<View>(R.id.recyclerviewlayout)
                    layoutview.removeView(rv)
                    //LayoutInflater.from(this).inflate(R.layout.recyclerview,layoutview,true)
                    layoutview.addView(rv)
                    rv = findViewById<View>(R.id.recyclerviewlayoutRV) as RecyclerView
                    rv.layoutManager = LinearLayoutManager(this)
                    rv.adapter = rv_ClusterSearchAdapter(SearchResultList)

                }

            }


        }




    }
}