odoo.define('pos_product_rating.rating', function (require) {
"use strict";


    var models = require('point_of_sale.models');



    //    loading field prodcut ratings to pos
    models.load_fields("product.product", ['product_ratings']);
    console.log("hiii",models)
    console.log("prodcut")
//    console.log("product rating",product.product_ratings)

     //    adding the field discount_tag in the receipt
//    var _super_orderline = models.Orderline.prototype;
//    models.Orderline = models.Orderline.extend({
//        export_for_printing: function() {
//            var line = _super_orderline.export_for_printing.apply(this,arguments);
//            line.product_ratings = this.get_product().product_ratings;
//            return line;
//        },
//    });


});