odoo.define('pos_order_history.ShowOrdersWidget', function (require) {
"use strict";
var gui = require('point_of_sale.gui');
var chrome = require('point_of_sale.chrome');
var core = require('web.core');
var models = require('point_of_sale.models');
var PosModelSuper = models.PosModel;
var pos_screens = require('point_of_sale.screens');
var QWeb = core.qweb;
var _t = core._t;

var ShowOrdersWidget = pos_screens.ScreenWidget.extend({
        template: 'ShowOrdersWidget',
        init: function(parent, options){
            this._super(parent, options);
            this.order_string = "";
        },

        auto_back: true,
        show: function(){
            var self = this;
            this._super();
            this.renderElement();
            this.$('.back').click(function(){
                self.gui.back();
            });
//            ['partner_id','=',this.pos.get_client()]
            var pos_orders = this.pos.pos_orders;
            this.render_list(pos_orders);
                 console.log("pos orders",pos_orders)

        },

        render_list: function(orders){
             var self = this;
                for(var i = 0, len = Math.min(orders.length,1000); i < len; i++) {
                    if (orders[i]) {
                        var order = orders[i];
                        self.order_string += i + ':' + order.pos_reference + '\n';
                    }
                }


            var contents = this.$el[0].querySelector('.show-order-list-lines');
            console.log("ii",orders)9
            if (contents){
                contents.innerHTML = "";
                for(var i = 0, len = Math.min(orders.length,1000); i < len; i++) {


                   if (orders[i]) {




                    var order = orders[i];
                    console.log("hii",this.pos.get_client().id);
                      console.log("p_id",order.partner_id[0])

//                    console.log("p_id",order.partner_id[0])

                    var clientline_html = QWeb.render('ShowOrderLines', {widget: this, order: order});
                    var orderline = document.createElement('tbody');
                    orderline.innerHTML = clientline_html;
                    orderline = orderline.childNodes[1];
                    contents.appendChild(orderline);
                   }
                }
            }
        },
    });
    gui.define_screen({name:'ShowOrdersWidget', widget: ShowOrdersWidget});
    return {
        ShowOrdersWidget: ShowOrdersWidget
    }
});
