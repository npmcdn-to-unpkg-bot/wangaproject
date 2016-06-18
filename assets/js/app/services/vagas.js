app.factory('CursosService',function($http){
    return $http.get('/api/cursos/')
        .success(function(data){
            return data;
        })
        .error(function(err){
            return err;
        })
});
