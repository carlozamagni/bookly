/**
 * Created by carlozamagni on 24/08/14.
 */

var booklyApp = angular.module('booklyApp', ['ngRoute'], function($interpolateProvider) {
    // custom delimiters to avoid collision with jinja2
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});


booklyApp.controller('SearchCtrl', function($scope, $http) {

    var isbnQuerystringArg = '';
    var fulltextQuerystringArg = '';

    if($scope.isbn != null){
        isbnQuerystringArg = 'isbn=' + $scope.isbn;
    }

    if($scope.fulltext != null){
        fulltextQuerystringArg = 'q=' + $scope.fulltext;
    }

    var searchUrl = '/catalog/search?' + fulltextQuerystringArg + '&' + isbnQuerystringArg;

    $http.get(searchUrl)
       .then(function(res){
            $scope.item = res.data;

            $scope.item['selectedQuantity'] = 0;
            $scope.item['selectedColor'] = 'ffffff';

            /*
            $scope.item.colors.push({code:'ffffff', name:'White'})
            $scope.item.colors.push({code:'FF2646', name:'Pinky Red'})
            */
            console.log($scope.item);
        });



});