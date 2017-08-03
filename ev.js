function __get_event_env__() {
    //pyimport time;
    var id = 0;
    var sh = [];
    function add_event(func, args, interval, id) {
        var ev = [func, args, time.time()+interval/1000., id];
        sh.push(ev);
    }
    function clear_event(id) {
        var to_del = false;
        for (var i=0; i<sh.length; i++) {
            if (sh[i][3] === +id) {
                to_del = i;
                break;
            }
        }
        if (to_del !== false) {
            sh.splice(to_del, 1);
        }
    }
    function exec_one() {
        var t = time.time();
        for (var i=0; i<sh.length; i++) {
            if (sh[i][2] <= t) {
                try {
                    sh[0].call(this, sh[1]);
                } catch (e) {
                    // todo what should we do in case of errors?
                }
                clear_event(sh[3]);
                break
            }
        }
    }
    function setTimeout(func, interval) {
        var args = [];
        var my_id = ++id;
        add_event(func, args, interval, my_id);
        return my_id  // todo return a full timeout object
    }
    function setInterval(func, interval) {
        var args = [];
        var my_id = ++id;
        function wrap() {
            try {
                func.call(this, args);
            } finally {
                add_event(wrap, [], interval, my_id)
            }
        }
        add_event(wrap, [], interval, my_id);
        return my_id // todo return a full timeout object
    }

    function event_loop() {
        while (true) {
            if (sh.length===0) {
                break
            }
            exec_one();
            time.sleep(0.001);

        }
    }
    function clearInterval(timeoutObj) {
        clear_event(timeoutObj);
    }
    var clearTimeout = clearInterval;

    return [setTimeout, clearTimeout, setInterval, clearInterval, event_loop]
}
__event_env__ = __get_event_env__();
var setTimeout = __event_env__[0];
var clearTimeout = __event_env__[1];
var setInterval = __event_env__[2];
var clearInterval = __event_env__[3];
var __event_loop__ = __event_env__[4];

setTimeout(function h() {console.log('aaa')}, 1000);


__event_loop__()