app.controller('CursosController', ['$scope','$http','$location', function($scope,$http,$location){
	var vm = this;
	vm.cursos = []; //declare an empty array
	vm.page = 1; // initialize page no to 1
	vm.total = 0;
	vm.pageSize = 10; //this could be a dynamic value from a drop down
	$scope.pageSize = vm.pageSize;
	vm.getData = function(page, pageSize){ // This would fetch the data on page change.
		//In practice this should be in a factory.
		console.log({page, pageSize});
		vm.cursos = [];
		$http.get("/v1/cursos/?page="+page).success(function(response){
			vm.cursos = response.results;  //ajax request to fetch data into vm.data
			vm.total = response.count;
		});
	};
	vm.getData(vm.page,vm.pageSize); // Call the function to fetch initial data on page load.
}])
