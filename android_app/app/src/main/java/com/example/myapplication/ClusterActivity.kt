package com.example.myapplication

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.widget.Button
import android.widget.Toast
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.myapplication.R
import com.github.kittinunf.fuel.Fuel
import com.github.kittinunf.fuel.coroutines.awaitStringResponse
import com.github.kittinunf.fuel.httpGet
import com.github.kittinunf.result.Result
import kotlinx.coroutines.runBlocking
import org.json.JSONArray
import org.json.JSONObject


class ClusterActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.clusters)

        val username = getIntent().getStringExtra("username");

        val cluster_list = mutableListOf<Cluster>()

        val site_url = "http://10.0.2.2:8000/API/cluster_get/" + username

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

                        var st = String(response.data);

                        var a = JSONArray(st)

                        for(i in 0 until a.length()) {
                            val obj = a.getJSONObject(i)

                            cluster_list.add(Cluster(obj.get("cluster_name").toString(),""));
                        }

                        val rv_cluster = findViewById<View>(R.id.rvClusterList) as RecyclerView
                        rv_cluster.layoutManager = LinearLayoutManager(this)
                        rv_cluster.adapter = rv_ClusterAdapter(cluster_list)


                    }
                }
            }
    }
}