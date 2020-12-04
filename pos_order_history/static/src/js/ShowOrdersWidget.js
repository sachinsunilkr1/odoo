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

//loads models
models.load_models({
            model: 'pos.order',
            fields: ['id', 'name', 'session_id', 'state', 'pos_reference', 'partner_id', 'amount_total','lines', 'amount_tax','sequence_number', 'fiscal_position_id', 'pricelist_id', 'create_date'],
            domain: function(self){ return [['company_id','=',self.company.id]]; },
            loaded: function (self, pos_orders) {
            var orders = [];
            for (var i in pos_orders){
                orders[pos_orders[i].id] = pos_orders[i];
                console.log("models loaded",pos_orders[i].partner_id[0])

            }
            self.pos_orders = orders;
            self.order = [];
            for (var i in pos_orders){
                self.order[i] = pos_orders[i];

            }


        },

    });

//loads the newly created order into models
models.PosModel = models.PosModel.extend({
  _save_to_server: function (orders, options) {
   var result_new = PosModelSuper.prototype._save_to_server.call(this, orders, options);
   var self = this;
   var new_order = {};
   var orders_list = self.pos_orders;
    for (var i in orders) {
      var partners = self.partners;

      var partner = "";
      for(var j in partners){
           if(partners[j].id == orders[i].data.partner_id){
                partner = partners[j].name;
             }
         }
            new_order = {
                'amount_tax': orders[i].data.amount_tax,
                'amount_total': orders[i].data.amount_total,
                'pos_reference': orders[i].data.name,
                'partner_id': [orders[i].data.partner_id, partner],
                'session_id': [self.pos_session.id, self.pos_session.name]
            };
            orders_list.push(new_order);
            self.pos_orders = orders_list;
            self.gui.screen_instances.ShowOrdersWidget.render_list(orders_list);
        }
        return result_new;
    },
});

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
        },
        render_list: function(orders){
            var contents = this.$el[0].querySelector('.show-order-list-lines');
            if (contents){
                contents.innerHTML = "";
                for(var i = 0, len = Math.min(orders.length,1000); i < len; i++) {
                    if (orders[i]) {
                    console.log("call this",this)
                    var ab=this.pos.get_client().id;

                    if(!ab){


                                    var order = orders[i];
                                    var clientline_html = QWeb.render('ShowOrderLines', {widget: this, order: order});
                                    var orderline = document.createElement('tbody');
                                    orderline.innerHTML = clientline_html;
                                    orderline = orderline.childNodes[1];
                                    contents.appendChild(orderline);

                    }

                    else if(orders[i].partner_id[0] == this.pos.get_client().id){
                                    var order = orders[i];
                                    var clientline_html = QWeb.render('ShowOrderLines', {widget: this, order: order});
                                    var orderline = document.createElement('tbody');
                                    orderline.innerHTML = clientline_html;
                                    orderline = orderline.childNodes[1];
                                    contents.appendChild(orderline);
                    }

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
