odoo.define('pos_product_rating.rating', function (require) {
"use strict";

    var screens = require('point_of_sale.screens');
	var core = require('web.core');
	var QWeb = core.qweb;
    var models = require('point_of_sale.models');



    //    loading field prodcut ratings to pos
    models.load_fields("product.product", ['product_ratings']);
    console.log(" rating models",models)


     var _super_order = models.Orderline.prototype;
        models.Orderline = models.Orderline.extend({
            export_for_printing: function() {

                var line = _super_order.export_for_printing.apply(this,arguments);
                console.log("line1", line);

                line.product_ratings = this.get_product().product_ratings;
                console.log("line2", line.product_ratings);
                return line;
            },

    });








});