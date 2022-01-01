package com.example.myapplication

import android.content.Intent
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

class rv_ClusterSearchAdapter(val datalist:MutableList<SearchResult>) : RecyclerView.Adapter<rv_ClusterSearchAdapter.ViewHolder>() {

    class ViewHolder( val itemview : View) : RecyclerView.ViewHolder(itemview){
        val resUrl = itemview.findViewById<TextView>(R.id.Cluster_Name)
        val resText = itemview.findViewById<TextView>(R.id.Cluster_Strategy)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val inflater = LayoutInflater.from(parent.context)
        val view = inflater.inflate(R.layout.cluster_rv_layout,parent,false)
        return ViewHolder(view)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        val clusterItem = datalist[position]

        holder.resUrl.setText(clusterItem.url)
        holder.resText.setText(clusterItem.text)

        //holder.itemview.setOnClickListener() {}
    }

    override fun getItemCount(): Int {
        return datalist.size
    }

}