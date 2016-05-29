app.controller('VagaController', ['$scope','CursosService',function($scope,CursosService){
    CursosService.success(function(data){
        $scope.cursos = data;
    });
}])
