#include <bits/stdc++.h>
using namespace std;

class graph_matrix{
public:
	int nodes;
	vector<vector<int> > v;
	graph_matrix(int kitne_nodes){
		nodes = kitne_nodes;
		// n*n ka vector bana diya

		v.resize(kitne_nodes);
		for(int i=0;i<kitne_nodes;i++){
			v[i].resize(kitne_nodes);
		}

		// node is connected to itself
		for(int i = 0;i<kitne_nodes;i++){
			v[i][i] = 1;
		}
	}

	void print(){
		for(int i = 0;i<v.size();i++){
			for(int j = 0;j<v[i].size();j++){
				cout<<v[i][j]<<" ";
			}
			cout<<endl;
		}
	}

	void addedge(int a,int b){
		v[a][b] = 1;
		v[b][a] = 1;
	}

};


class graph{
public:
	vector<vector<int> > v;
	int nodes;
	graph(int n){
		nodes = n;
		v.resize(n);
	}

	void addedge(int a,int b){
		v[a].push_back(b);
		v[b].push_back(a);
	}

	void __dfs(int node,vector<bool> &isvisited){
		if(isvisited[node] == true){
			return;
		}

		else {

			cout<<node << "-->";
			isvisited[node] = true;

			for (int i = 0; i < v[node].size(); ++i)
			{
				__dfs(v[node][i],isvisited);
			}
		}

		return;
	}

	void dfs(int start_node){
		vector<bool> isvisited(nodes);
		__dfs(start_node,isvisited);

		for (int i = 0; i < nodes; ++i)
		{
			__dfs(i,isvisited);
		}
	}




	void bfs(int sn){
		vector<bool> isvisited(nodes);
		queue<int> q;
		q.push(sn);
		while(q.empty() == false){
			int curr = q.front();
			q.pop();
			if(isvisited[curr] == true){
				continue;
			}
			isvisited[curr] = true;
			cout<<curr<<"-->";
			for (int i = 0; i < v[curr].size(); ++i)
			{
				if(isvisited[v[curr][i]] == false)
					q.push(v[curr][i]);
			}
		}

	}

};


int main(){

	graph g(5);
	// g.print();
	g.addedge(0,1);
	g.addedge(1,2);
	g.addedge(2,3);
	g.addedge(3,4);
	// g.dfs(1);
	cout<<endl;
	g.bfs(0);
	// g.print();

}