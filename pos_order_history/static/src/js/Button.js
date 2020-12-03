odoo.define('pos_order_history.Button', function (require) {
"use strict";

var core = require('web.core');
var pos_screens = require('point_of_sale.screens');
var models = require('point_of_sale.models');
var field_utils = require('web.field_utils');
var gui = require('point_of_sale.gui');
var chrome = require('point_of_sale.chrome');
var _t = core._t;
var QWeb = core.qweb;
var PosModelSuper = models.PosModel;





models.load_models({
    model: 'pos.order',
    fields: ['id', 'name', 'session_id', 'state', 'pos_reference', 'partner_id', 'amount_total','lines', 'amount_tax','sequence_number', 'fiscal_position_id', 'pricelist_id', 'create_date'],
    domain: function(self){ return [['company_id','=',self.company.id]]; },
    loaded: function (self, pos_orders) {
        var orders = [];


        for (var i in pos_orders){
            orders[pos_orders[i].id] = pos_orders[i];
        }
        self.pos_orders = orders;
        self.order = [];
        for (var i in pos_orders){
            self.order[i] = pos_orders[i];



        }


    },
});
//var PosSuperModel = models.PosModel.prototype;
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




var ShowOrderButton = pos_screens.ActionButtonWidget.extend({
    template: 'ShowOrderButton',
    button_click: function(){
        this.gui.show_screen('ShowOrdersWidget')



    }


});
pos_screens.define_action_button({
    'name': 'Show Order',
    'widget': ShowOrderButton,
    'condition': function(){
        return this.pos;
    },
});

});
