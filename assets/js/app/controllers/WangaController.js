app.controller('WangaController',function($scope,$mdSidenav){
    //toggleNav()
    //md-component-id="rightnav"

    $scope.toggleNav = function () {
      // Component lookup should always be available since we are not using `ng-if`
      $mdSidenav('rightnav').toggle();
    };

});
