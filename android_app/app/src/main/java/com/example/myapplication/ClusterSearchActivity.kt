package com.example.myapplication

import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.LinearLayout
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.constraintlayout.widget.ConstraintLayout
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.github.kittinunf.fuel.Fuel
import com.github.kittinunf.result.Result
import org.json.JSONArray
import org.json.JSONObject

class ClusterSearchActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        supportActionBar?.hide()
        setContentView(R.layout.cluster_search)

        var searchClicked = false

        val layoutview = findViewById<View>(R.id.thisview) as LinearLayout
        val SearchButton  = findViewById<Button>(R.id.ClusterSearchButton) as Button

        val username  = getIntent().getStringExtra("username")!!
        val cluster_name = getIntent().getStringExtra("cluster_name")!!
        val depth = getIntent().getStringExtra("depth")!!.toInt()

        println("user:${username} , clust: ${cluster_name}, ${depth}")



        SearchButton.setOnClickListener(){

            var searchtext = findViewById<EditText>(R.id.editTextInput) as EditText

            if(searchtext.text.toString() != ""){

                //do api call here then populate SearcResultList with SearchResult objects

                val SearchResultList = mutableListOf<SearchResult>()
                SearchResultList.add(SearchResult("A url","A text"))
                SearchResultList.add(SearchResult("A url 2","A text 2"))

                val site_url = "http://10.0.2.2:8000/API/searchtext/?user_name=${username}&clusters=${cluster_name}&depth=${depth}&searchtext=${searchtext.text.toString()}"

                Log.d("url", site_url)

                Fuel.get(site_url)
                    .response { request, response, result ->
                        when (result) {
                            is Result.Failure -> {
                                Toast.makeText(
                                    this,
                                    "Error. Couldn't connect to api",
                                    Toast.LENGTH_SHORT
                                ).show()
                            }
                            is Result.Success -> {

                                var st = JSONObject( String(response.data))

                                var msg = (st.get("msg"))

                                println(msg)

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


        }




    }
}