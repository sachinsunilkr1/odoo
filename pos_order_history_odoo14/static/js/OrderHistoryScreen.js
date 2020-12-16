odoo.define('pos_order_history.OrderHistoryScreen', function (require) {
    'use strict';

    const Registries = require('point_of_sale.Registries');
    const IndependentToOrderScreen = require('point_of_sale.IndependentToOrderScreen');
    const { useListener } = require('web.custom_hooks');
    const { posbus } = require('point_of_sale.utils');
    var rpc = require('web.rpc');
    var models = require('point_of_sale.models');
    var PosModelSuper = models.PosModel;
    const ProductScreen = require('point_of_sale.ProductScreen');


 models.load_fields('pos.order', ['create_date']);



    var _super_orderline = models.Orderline.prototype;
    models.Orderline = models.Orderline.extend({
        _save_to_server : function() {
            var line = _super_orderline._save_to_server.apply(this,arguments);
            line.create_date = moment(order.creation_date).format('YYYY-MM-DD hh:mm A');
             console.log("iiii",line)
            return line;
        },
    });






    class OrderHistoryScreen extends IndependentToOrderScreen {
        constructor() {
            super(...arguments);

        }
        get orderList() {

            return this.env.pos.get_order_list();
        }
        getDate(order) {
            return moment(order.creation_date).format('YYYY-MM-DD hh:mm A');
        }

    }
    OrderHistoryScreen.template = 'OrderHistoryScreen';

    Registries.Component.add(OrderHistoryScreen);

    return OrderHistoryScreen;
});
